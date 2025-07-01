import streamlit as st
import pandas as pd

@st.cache_data
def load_data():
    # Load CSV with Turkish-compatible encoding and correct separator
    df = pd.read_csv("mbg430_grades.csv", encoding='iso-8859-9', sep=';')
    df.columns = df.columns.str.strip()  # Clean column names
    df['student_id'] = df['student_id'].astype(str).str.split(".").str[0]  # Clean Student IDs
    return df

# Load data
df = load_data()

# App Title
st.title("📋 MBG430 Student Grade Lookup")
st.write("Please enter your Student ID to view your final grade:")

# User input
entered_id = st.text_input("Enter Student ID:")

# Button
if st.button("Show Grade"):
    result = df[df['student_id'] == entered_id]

    if result.empty:
        st.error("❌ No record found for this Student ID.")
    else:
        st.success("✅ Record found!")
        # Show only final grade (adjust column name if needed)
        final_result = result[["name surname",'final_grade']].reset_index(drop=True)
        st.dataframe(final_result)

