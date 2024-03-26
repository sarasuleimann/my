import streamlit as st
from langchain.langchain import LangChain
import requests
import PyPDF2

# Initialize LangChain with Google Gemini API
langchain = LangChain(model="google/gemini", max_length=100)

# Function to generate response from LangChain
def generate_response(user_input):
    response = langchain.generate(user_input, max_length=50)
    return response

# Function to extract text from uploaded PDF
def extract_text_from_pdf(uploaded_file):
    with open(uploaded_file.name, "rb") as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        text = ""
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
    return text

# Streamlit UI
def main():
    st.title("LLM Chat App with PDF Integration")

    user_input = st.text_input("You:", "")
    response = ""

    if st.button("Send"):
        response = generate_response(user_input)
        st.text_area("LLM:", value=response, height=200)

    st.sidebar.title("PDF Upload")
    uploaded_file = st.sidebar.file_uploader("Upload PDF", type=["pdf"])

    if uploaded_file is not None:
        st.sidebar.write("File Uploaded Successfully!")
        text_from_pdf = extract_text_from_pdf(uploaded_file)
        st.sidebar.text_area("Text from PDF:", value=text_from_pdf, height=200)

if __name__ == "__main__":
    main()
