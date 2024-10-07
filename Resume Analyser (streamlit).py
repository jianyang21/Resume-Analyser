import pypdf
import streamlit as st
import re
import pymongo
from pymongo import MongoClient


# MongoDB connection setup
client = MongoClient("mongodb://localhost:27017/")
db = client['ResumeDB']
collection = db['ResumeData']


# Streamlit application title
st.title("Resume Analyser")

# User inputs skills
st.write("What are the skills you have?")
given_skills = st.multiselect(
    "Skills:", 
    ['SQL', 'Tableau', 'Machine Learning', 'Data Analysis', 'Python', 'R', 'Power BI', 'NoSQL', 'AWS', 'Docker', 'Streamlit']
)

# Display number of selected skills
st.success(f"Total number of skills selected: {len(given_skills)}")

# User inputs role
st.header("Enter the role you are applying for:")
role = st.text_input("Role:")

# Upload Resume section
st.header("Upload your Resume")
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")


# Function to extract Gmail addresses
def extract_gmail_addresses(content):
    pattern = r'\b[a-zA-Z0-9._%+-]+@gmail\.com\b'
    gmail_addresses = re.findall(pattern, content)
    return gmail_addresses

# Function to extract phone numbers
def extract_phone_numbers(content):
    phone_pattern = r'\b\d{10}\b|\b(?:\d{3}[-.\s]?){2}\d{4}\b'
    phone_numbers = re.findall(phone_pattern, content)
    return phone_numbers

# Extract content from the PDF and identify Gmail and phone numbers
if uploaded_file is not None:
    reader = pypdf.PdfReader(uploaded_file)
    all_content = ""
    for page in reader.pages:
        content_text = page.extract_text()
        all_content += content_text

    gmail_addresses = extract_gmail_addresses(all_content)
    phone_number = extract_phone_numbers(all_content)

    # Display Gmail addresses
    if gmail_addresses:
        st.write("Gmail addresses found in the resume:")
        st.write(gmail_addresses)
    else:
        st.write("No Gmail addresses found.")

    # Display phone numbers
    if phone_number:
        st.write("Phone number of the applicant:")
        st.write(phone_number)
    else:
        st.write("No phone number found.")

# Extract the 'Skills' section from the resume
if uploaded_file is not None:
    reader = pypdf.PdfReader(uploaded_file)
    skills_section_found = False
    skills_text = ""
    end_keywords = ["experience", "education", "projects", "certifications"]

    for page_num, page in enumerate(reader.pages):
        text = page.extract_text()

        if "skills" in text.lower():
            skills_section_found = True
            start_idx = text.lower().find("skills")
            skills_text = text[start_idx:]

            # Stop at the next section based on the end keywords
            for keyword in end_keywords:
                keyword_idx = skills_text.lower().find(keyword)
                if keyword_idx != -1:
                    skills_text = skills_text[:keyword_idx]
                    break
            break

    if skills_section_found:
        st.write("Extracted 'Skills' section:")
        st.write(skills_text.strip())

        extracted_skills = set(skill.strip().lower() for skill in skills_text.split(','))
        missing_skills = set(given_skills) - extracted_skills
    else:
        st.write("No 'Skills' section found.")
else:
    st.write("Please upload a PDF file to extract the Skills section.")

# Submit the extracted data to MongoDB
if st.button("Submit"):
    document = {
        "Role": role,
        "Skills": list(extracted_skills),
        "Gmail": gmail_addresses,
        "Phone No": phone_number
    }

    data = collection.insert_one(document)

    if data.acknowledged:
        st.success("Submitted")
    else:
        st.error("Error")

    

