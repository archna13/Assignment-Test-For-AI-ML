# Assignment-Test-For-AI-ML
# Gen-AI MongoDB Query System using Offline LLM

This project is a Gen-AI assignment that demonstrates how to build an automated data query and retrieval system using:
- An offline LLM (CodeLLaMA)
- MongoDB
- Python
- CSV file data

It allows natural language questions about CSV data to be dynamically converted into MongoDB queries, executed, and either displayed or saved.

---

## 📦 Features

✅ Load CSV into MongoDB  
✅ Generate MongoDB queries using an offline LLM  
✅ Display or save results to CSV  
✅ Store all generated queries in a log file  
✅ Built-in error handling and flexibility

---

## 🛠 Setup Instructions

### 1. Clone the Repository or Prepare Files

Ensure you have:
- `llm_task.py` (main script)
- `sample_data.csv` (your dataset)

### 2. Install Requirements

```bash
pip install pandas pymongo transformers torch

### Running the App
To launch the interactive interface:


python llm_task.py

Then follow on-screen prompts:

Enter a question about your dataset.

Choose whether to display or save the result.

Outputs are saved as test_caseX.csv files.

Generated queries are saved in Queries_generated.txt.
