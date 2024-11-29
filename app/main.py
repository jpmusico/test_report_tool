import streamlit as st
import os
import pandas as pd
import plotly.express as px

from openai_helper import generate_insights

# Set up main app title
st.title("Test Execution Report Tool")

# Path to the data folder
DATA_PATH = "./data"

# List projects
st.sidebar.title("Projects")
projects = [f for f in os.listdir(DATA_PATH) if os.path.isdir(os.path.join(DATA_PATH, f))]

if projects:
    # Select a project
    selected_project = st.sidebar.selectbox("Select a Project", projects)
    project_path = os.path.join(DATA_PATH, selected_project)
    
    # Get all CSV files for the selected project
    csv_files = [f for f in os.listdir(project_path) if f.endswith('.csv')]
    
    if csv_files:
        # Dataframe to hold all aggregated data
        aggregated_data = pd.DataFrame()

        for file in csv_files:
            file_path = os.path.join(project_path, file)
            
            # Extract build ID and timestamp from the filename
            parts = file.split('_')
            build_id = parts[1]
            timestamp = parts[2].split('.')[0]
            
            # Load data from CSV
            data = pd.read_csv(file_path)
            
            # Add new columns for 'Build ID' and 'Timestamp'
            data['Build ID'] = build_id
            data['Timestamp'] = timestamp
            
            # Append to the aggregated DataFrame
            aggregated_data = pd.concat([aggregated_data, data], ignore_index=True)
        
        # Check if 'status' column exists
        if "status" in aggregated_data.columns:
            # Grouping by Build ID and Status, then count occurrences
            status_summary = aggregated_data.groupby(['Build ID', 'status']).size().reset_index(name='Count')
            
            # Pivoting the data so 'status' values become columns
            pivoted_data = status_summary.pivot_table(
                index='Build ID', 
                columns='status', 
                values='Count', 
                fill_value=0
            )
            
            # Resetting index for a flat structure
            pivoted_data = pivoted_data.reset_index()

            # Display the aggregated bar chart
            st.subheader("Aggregated Test Status by Build ID")
            # st.write(pivoted_data)  # Optional: To inspect the final pivoted data
            st.bar_chart(pivoted_data.set_index('Build ID'))

            # Grouping by tc_id and getting the latest entry based on execution_end
            aggregated_data['execution_end'] = pd.to_datetime(aggregated_data['execution_end'])
            latest_status = aggregated_data.sort_values('tc_id', ascending=True) \
                                           .drop_duplicates(subset='tc_id', keep='first') \
                                           [['tc_id', 'status', 'execution_end']]
            
            # Display the latest status for each tc_id
            st.subheader("Latest Test Status per Test Case (tc_id)")
            st.dataframe(latest_status)
            # Aggregating the count of each status for the pie chart
            status_counts = latest_status['status'].value_counts().reset_index()
            status_counts.columns = ['Status', 'Count']

            # Create a pie chart using Plotly
            fig = px.pie(status_counts, names='Status', values='Count', title='Test Status Distribution')
            
            # Display the pie chart in Streamlit
            st.plotly_chart(fig)

        else:
            st.write("No 'status' column found for aggregation.")

        # Display the combined data
        st.subheader(f"Aggregated Data for {selected_project}")
        st.dataframe(aggregated_data)

        st.subheader("Automated Test Insights")
        if not aggregated_data.empty:
            if st.button("Generate Insights"):
                insights = generate_insights(aggregated_data)
                st.text_area("Test Execution Insights", insights, height=200)
        else:
            st.write("No data available for insights.")
        
    else:
        st.warning(f"No CSV files found in {selected_project}.")
else:
    st.warning("No projects found in the data folder.")
