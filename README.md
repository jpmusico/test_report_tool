---

# 🧪 Test Execution Report Tool

**Test Execution Report Tool** is an interactive web application built with **Streamlit** that simplifies the analysis of test execution data stored in CSV files. Designed for QA teams and managers, it dynamically aggregates data, generates insightful visualizations, and provides detailed reporting to monitor test case execution trends.

---

## 🌟 Features

- **Project-Based Organization**: Supports multiple projects with CSV files organized by folders.
- **Dynamic Visualizations**:
  - Aggregated bar charts for test status per build.
  - Pie charts showing the distribution of latest test statuses.
- **Detailed Reporting**:
  - Automatically merges test execution results from multiple CSV files.
  - Displays the latest status of test cases (`tc_id`) based on execution timestamps.
- **Interactive UI**: Streamlined navigation and data exploration for QA professionals.
- **Automated Test Insights and Suggestions**: Generate natural language summaries of test results.
  - Use OpenAI APIs to analyze test execution data and provide summaries, such as:
      - "Build 1234 has a failure rate of 20%, with 5 critical test cases failing in the Login feature."
      - Highlight trends, common issues, or areas that need attention.

---

## 📂 Folder Structure

Ensure your data folder is structured like this:

```
project/
│
├── data/                          # Folder containing test execution CSV files
│   └── <project_name>/            # Subfolders for each project
│       └── BNK_001_20241126230234.csv
│
├── main.py                        # Streamlit app entry point
├── requirements.txt               # Python dependencies
└── README.md                      # Project description and instructions
```

- **CSV Naming Convention**: `<ProjectInitials>_<BuildID>_<Timestamp>.csv`
- **CSV Columns Required**: Ensure the following columns exist in your CSV files:
  - `execution_start`, `execution_end`, `tc_id`, `type`, `status`, `tester`, `priority`, `feature`, `category`

---

## 🚀 How to Run the App

### 1. Clone the Repository
Clone this repository to your local machine:
```bash
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>
```

### 2. Install Dependencies
Install the required Python libraries using pip:
```bash
pip install -r requirements.txt
```

### 3. Add Your Data
Place your project folders containing CSV files under the `data/` directory.

### 4. Create a .env file with your openai key
Content should be:
OPENAI_API_KEY=<your_key>

### 5. Start the Application
Run the Streamlit app:
```bash
streamlit run main.py
```

### 6. Open the App in Your Browser
Streamlit will launch the app automatically in your default web browser at `http://localhost:8501`.

---

## 🖼️ How to Use

1. Select a project from the sidebar. The app will load and process all CSV files in the corresponding project folder.
2. Explore the following features:
   - **Aggregated Data Table**: View merged test execution data from all CSV files in the project.
   - **Bar Chart**: See the status distribution of test cases across builds.
   - **Latest Test Case Status Table**: Check the latest status of each test case (`tc_id`).
   - **Pie Chart**: Visualize the overall distribution of the latest test statuses.
3. Use the interactive tables and charts to analyze your test execution trends.

---

## 🤝 Contributions

We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Submit a pull request.

---
