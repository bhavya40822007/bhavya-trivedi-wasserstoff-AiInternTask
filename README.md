# PDF Summarization and Keyword Extraction Pipeline
### Project Overview
This project is designed to process multiple PDFs by extracting text from them, generating domain-specific summaries, extracting keywords, and storing the results in MongoDB. The pipeline is concurrent, allowing for the efficient processing of multiple documents simultaneously.
### Table of Contents
1. Project Overview
2. Features
3. Tech Stack
4. Installation Instructions
5. Usage
6. MongoDB Configuration
7. Concurrency & Performance
8. Error Handling
### Features
1 - PDF Ingestion: Download and process multiple PDFs from URLs listed in a JSON file.

2 - Text Extraction: Extract text from each PDF using PyPDF2.

3 - Summarization: Use the spaCy NLP model to generate summaries.

4 - Keyword Extraction: Extract important keywords using TF-IDF.

5 - MongoDB Storage: Store file metadata, summaries, and keywords in MongoDB.

6 - Concurrency: Utilize Python’s concurrent.futures to process multiple PDFs in parallel.
### Tech Stack
i- Python 3.7+

ii - PyPDF2: For PDF text extraction.

iii - spaCy: For NLP-based text summarization.

iv - scikit-learn (TF-IDF): For keyword extraction.

v - MongoDB: For storing metadata, summaries, and keywords.

vi - ThreadPoolExecutor: For concurrent PDF processing.
### Installation Instructions - 
#### 1. Clone the Repository
First, clone the repository to your local environment using Git:
    git clone https://github.com/yourusername/wasserstoff-ai-intern-task.git
    
    cd wasserstoff-ai-intern-task
#### 2. Install Required Dependencies - 
Make sure you have pip installed, then install the required libraries:

    pip install PyPDF2 spacy sklearn pymongo requests
#### 3. Download the spaCy Language Model -
Install the English language model for spaCy:

    python -m spacy download en_core_web_sm
### Usage
#### 1. Dataset Preparation
Make sure your Dataset.json is located in the root directory. The Dataset.json file should contain URLs for PDFs, for example:

{
   "pdf1": "https://example.com/pdf1.pdf",
   "pdf2": "https://example.com/pdf2.pdf"
}
#### 2. Running the Pipeline - 
Run the main Python script to process the PDFs:

    python main.py
### MongoDB Configuration
#### 1. Local MongoDB Setup
If you don’t have MongoDB installed, install it from here. Ensure MongoDB is running locally or use a cloud instance.

#### 2. Connecting to MongoDB
The script uses MongoDB for storing PDF metadata, summaries, and keywords. You can change the connection URI to point to a remote MongoDB instance by modifying the MongoDB connection string in the script:

    client = MongoClient('mongodb://localhost:27017/')
    db = client['pdf_summary_db']

### Concurrency & Performance - 
This pipeline uses Python's concurrent.futures.
ThreadPoolExecutor to process multiple PDFs concurrently.
You can control the number of concurrent workers by adjusting the max_workers argument in the code. By default, it's set to 5:

    with ThreadPoolExecutor(max_workers=5) as executor:
### Error Handling - 
1 . The pipeline includes basic error handling for common issues:

2 . Failed PDF downloads (e.g., network issues).

3 . Errors during text extraction or summarization.

4 . All errors are logged to the console with descriptive messages, and the program will skip over problematic PDFs.

    
