from dotenv import load_dotenv
import openai
import os

# Load .env file
load_dotenv()
# Retrieve the API key
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("API key not found. Please set the OPENAI_API_KEY environment variable.")

# Set the OpenAI API key
openai.api_key = openai_api_key

def generate_insights(dataframe):
    # Aggregate data for the summary
    total_tests = len(dataframe)
    passed_tests = len(dataframe[dataframe['status'] == 'pass'])
    failed_tests = len(dataframe[dataframe['status'] == 'fail'])
    deprecated_tests = len(dataframe[dataframe['status'] == 'deprecated'])
    not_ready_tests = len(dataframe[dataframe['status'] == 'not ready'])
    not_run_tests = len(dataframe[dataframe['status'] == 'not run'])
    feature_failures = dataframe[dataframe['status'] == 'fail']['feature'].value_counts().to_dict()
    
    # Prepare the input for OpenAI API
    prompt = f"""
    Generate a summary of the following test results:
    - Total tests executed: {total_tests}
    - Passed tests: {passed_tests}
    - Failed tests: {failed_tests}
    - Deprecated tests: {deprecated_tests}
    - Not Ready tests: {not_ready_tests}
    - Not Run tests: {not_run_tests}
    - Features with failures: {feature_failures}
    Provide a concise summary of the test execution results, highlighting key areas of improvement.
    """
    
    # Call the OpenAI API
    try:
        response = openai.chat.completions.create(
            model="gpt-4",  # Use "gpt-4" or "gpt-3.5-turbo" as needed
            messages=[
                {"role": "system", "content": "You are a helpful assistant for test management."},
                {"role": "user", "content": prompt}
            ]
        )
        # Extract the generated content
        generated_content = response.choices[0].message.content
        return generated_content
    except Exception as e:
        return f"Error generating insights: {e}"
