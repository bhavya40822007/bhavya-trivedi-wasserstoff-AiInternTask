# Parsing the Dataset.json file to extract PDfs
''' 
Step 1 - Cloning the github Repository to local environment -
        git clone https://github.com/yourusername/wasserstoff-ai-intern-task.git
'''

import json
file = 'C:/Users/WINDOWS 10/AI-Internship-Task/Dataset.json'
with open(file, 'r') as f:
    data = json.load(f)

# Extract PDF URLs from the JSON
pdf_urls = [entry["pdf_link"] for entry in data if 'pdf_link' in entry]
print(pdf_urls)


''' Step 2 - Download the PDFs - '''

import os
import requests

pdf_folder = "./AI-Internship-Task/pdfs"
os.makedirs(pdf_folder,exist_ok=True)

def download_pdf(pdf_url, folder_path):
    try:
        pdf_name = pdf_url.split("/")[-1]+".pdf"
        pdf_path = os.path.join(folder_path,pdf_name)
        response = requests.get(pdf_url)
        response.raise_for_status()

        # Save the PDF locally
        with open(pdf_path,'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {pdf_name}")
    except Exception as e:
        print(f"Falied to Download {pdf_url}: {e}")


#Download all PDFs from the extracted URLs
for pdf_url in pdf_urls:
    download_pdf(pdf_url,pdf_folder)

''' Step 3 - Extract Text From PDFs - '''

import PyPDF2
def extract_text(pdf_path);
    try:
        with open(pdf_path,'rb') as f:
            reader = PyPDF2.PdfReader(f)
            text = ""
            for i in reader.pages():
                text += i.extract_text()
        return text
    except Exception as e:
        print(f"Error extracting text from {pdf_path}: {e}")
        return None

''' Step 4 - Summarization and Keyword Extraction - '''
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer

nlp = spacy.load("en_core_web_sm")

def summarize(text):
    doc = nlp(text)
    summary = [ ]
    for i in doc.sents:
        summary.append(i.text)
    return "".join(summary[:5])

def extract_key(text):
    vec = TfidfVectorizer(stop_words="english",max_features=5)
    X = vec.fit_transform([text])
    return vec.get_feature_names_out()

''' Step 5 - Store Results in MongoDB '''
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['pdf_summary_db']
collection = db['pdf_documents']

def store_meta_Mongodb(pdf_name,summary,keywords):
    doc = {
        "file_name": pdf_name,
        "summary": summary,
        "keywords": keywords,
    }
    collection.insert_one(doc)
    print(f"Inserted data for {pdf_name} into MongoDB")

''' Step 6 - Process all PDFs - '''

def process_pdf(pdf_file):
        pdf_path = os.path.join(pdf_folder,pdf_file)
        print(f"Processing: {pdf_file}")

     

        #Extract text from the PDF
        t = extract_text(pdf_path)
        if t:
            # summarize the text
            summary = summarize(t)

            # extract keywords
            keywords = extract_key(t)

            # store results in MongoDB
            store_meta_Mongodb(pdf_file,summary,key)

''' Step 7 - Concurrency Processing and Error Handling - '''

# Using ThreadPoolExecutor for Concurrent processing -
from concurrent.futures import ThreadPoolExecutor, as_completed
results = []
with ThreadPoolExecutor(max_workers=5) as executor:
    f_key = {executor.submit(process_pdf,pdf_file): i for i in os.listdir(pdf_folder) if pdf_file.endswith('.pdf')}

    for f in as_completed(f_key):
        pdf_file = f_key[f]
        try:
            f.result()
        except Exception as e:
            print(f"Error occured for {pdf_file}: {str(e)}")

print(" ALL documents Processed. ")