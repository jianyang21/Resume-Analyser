# Resume Analyzer

Resume Analyzer is a web application built with Streamlit and Python that extracts and analyzes the content of resumes in PDF format. It performs sentiment analysis on the "About" section of the resume to gauge the candidate's outlook and behavior, identifies contact information, and compares the skills mentioned in the resume with user-provided skills.

## Features

- **Upload Resume (PDF)**: Users can upload their resumes in PDF format.
- **Skill Extraction**: Extracts the "Skills" section from the uploaded resume and compares it with user-selected skills.
- **Gmail and Phone Number Extraction**: Automatically extracts Gmail addresses and phone numbers from the resume.
- **Sentiment Analysis**: Analyzes the "About" section of the resume using a sentiment analysis model to determine the candidate's attitude (optimistic, neutral, or pessimistic).
- **MongoDB Integration**: Stores the resume details (role, skills, Gmail, phone number) in a MongoDB database for further use.

## Technologies Used

- **Streamlit**: For building the web interface.
- **PyPDF2**: For extracting text from PDF files.
- **Regular Expressions (Regex)**: For extracting Gmail addresses and phone numbers.
- **Transformers (Hugging Face)**: For performing sentiment analysis using a pre-trained model.
- **MongoDB**: For storing extracted resume data.
  
## Installation

To get the project running on your local machine, follow the steps below:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/jianyang21/resume-analyzer.git
    cd resume-analyzer
    ```

2. **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use: venv\Scripts\activate
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up MongoDB:**
    - Install and start MongoDB if not already installed.
    - Create a new database named `ResumeDB` and a collection called `ResumeData`.

5. **Run the application:**
    ```bash
    streamlit run Resume Analyser (streamlit).py
    ```

6. **Open your browser** to view the app: `http://localhost:8501`.

## File Structure

```bash
.
├── app.py                  # Main application file
├── README.md               # This README file
├── requirements.txt        # Dependencies for the project
└── .gitignore              # Git ignore file
