# Assignment-Test-For-AI-ML
# Gen-AI MongoDB Query System (Offline LLM)

This project demonstrates an end-to-end automated data query and retrieval system using:
- ✅ Offline LLM (CodeLLaMA)
- ✅ MongoDB
- ✅ CSV data
- ✅ Python

---

## 📦 Features

- Convert natural language questions into MongoDB queries using an LLM
- Load and store CSV data in MongoDB
- Execute dynamic queries generated from user input
- Display or export query results as CSV
- Log all queries into a text file

---

## 🛠 Setup Instructions

### 1. Clone or Download the Files

Make sure you have:
- `genai_query_system.py` (main script)
- `sample_data.csv`

### 2. Install Dependencies

pip install pandas pymongo transformers torch
```

### 3. Prepare the MongoDB Server

- Either use a local MongoDB instance
- Or replace the URI in the script with your MongoDB Atlas connection string

---

## 🚀 How to Run

python genai_query_system.py
```

Follow the prompts to:
- Enter a natural language question
- Choose whether to display or save the results

---

## 🧪 Example Test Cases

1. Find all products with a rating below 4.5 that have more than 200 reviews and are offered by 'Nike' or 'Sony'
2. Which products in the Electronics category have a rating of 4.5 or higher and are in stock?
3. List products launched after Jan 1, 2022, in Home & Kitchen or Sports categories with ≥10% discount, sorted by price descending

---

## 📂 Output

- test_case1.csv
- test_case2.csv
- test_case3.csv
- Queries_generated.txt (logs all questions and generated queries)

---


