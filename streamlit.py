import streamlit as st
import pandas as pd
import json, torch, re, ast, os
from pymongo import MongoClient
from transformers import AutoTokenizer, AutoModelForCausalLM

# -----------------------------
# Load or download the model
# -----------------------------
@st.cache_resource
def load_model():
    model_name = "codellama/CodeLlama-7b-Instruct-hf"
    local_dir = "./model"
    if not os.path.exists(local_dir) or not os.listdir(local_dir):
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16, device_map="auto")
        tokenizer.save_pretrained(local_dir)
        model.save_pretrained(local_dir)
    else:
        tokenizer = AutoTokenizer.from_pretrained(local_dir)
        model = AutoModelForCausalLM.from_pretrained(local_dir, torch_dtype=torch.float16, device_map="auto")
    return tokenizer, model

# -----------------------------
# MongoDB Utils
# -----------------------------
def load_csv_to_mongodb(df, collection):
    json_data = json.loads(df.to_json(orient="records"))
    collection.drop()
    collection.insert_many(json_data)
    return df.columns.tolist()

def convert_query_to_dict(query_str):
    query_str = re.sub(r'([{\[\s,])([A-Za-z0-9_.$-]+)(:)', r'\1"\2"\3', query_str)
    query_str = re.sub(r'(:\s*)([A-Za-z_.$-][A-Za-z0-9_.$-]*)(?=\s*[},\]])', r'\1"\2"', query_str)
    try:
        return ast.literal_eval(query_str)
    except Exception:
        return {}

def generate_query(prompt, tokenizer, model):
    inputs = tokenizer.encode(prompt, return_tensors="pt").to("cuda")
    outputs = model.generate(inputs, max_new_tokens=300, pad_token_id=tokenizer.eos_token_id)
    result = tokenizer.decode(outputs[0])
    try:
        query = result.split('.find(')[1].split(')\n\\end{code}')[0].replace('\n','').replace(' ','').split(')`')[0]
        return query
    except:
        return "{}"

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🧠 Gen-AI MongoDB Query System")
st.write("Ask questions about your CSV data — no coding needed!")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.dataframe(df.head())

    # MongoDB Connection
    url = "mongodb://localhost:27017"  # Or your Atlas URI
    client = MongoClient(url)
    db = client["ProductDB"]
    collection = db["ProductCollection"]
    columns = load_csv_to_mongodb(df, collection)

    tokenizer, model = load_model()

    st.success("CSV loaded and model ready.")
    user_question = st.text_input("💬 Enter your question:")

    if st.button("Generate & Run Query"):
        if user_question.strip() == "":
            st.warning("Please enter a question.")
        else:
            prompt = f"Convert to MongoDB query: {user_question}. Valid columns are: {', '.join(columns)}."
            query = generate_query(prompt, tokenizer, model)
            st.code(query, language="json")

            query_dict = convert_query_to_dict(query)
            results = list(collection.find(query_dict))
            if results:
                df_result = pd.DataFrame(results).drop(columns=["_id"], errors="ignore")
                st.dataframe(df_result)
                st.download_button("📥 Download CSV", df_result.to_csv(index=False), file_name="query_output.csv")
            else:
                st.warning("No data found for the given query.")
