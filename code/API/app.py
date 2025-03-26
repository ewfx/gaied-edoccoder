from email import policy
from email.parser import BytesParser
from flask import Flask, jsonify, request # type: ignore
import requests # type: ignore
import time
import hmac
import hashlib
import base64
import json
import pathlib
import textwrap
import os
import google.generativeai as genai # type: ignore
from IPython.display import Markdown # type: ignore
from IPython.display import display # type: ignore

app = Flask(__name__)

# Gemini API base URL
BASE_URL = "https://api.gemini.com"


# Your Gemini API key and secret
genai.configure(api_key="AIzaSyCdwpwcogU71rVRLIX8sde0A2alWIcI7xM")

# model = genai.GenerativeModel('gemini-pro')
# Sample data
data = [
    {"id": 1, "name": "Item 1"},
    {"id": 2, "name": "Item 2"}
]
inputtext = "get amout, codinate from 'hi amount : 50. codinate 90'"
def to_markdown(text):
  text = text.replace('•', '  *')
  print(text)
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# Home route
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Get all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(data)

# Get a single item by ID
@app.route('/getAttributeFromEMLFilepath', methods=['GET'])
def get_attribute_from_emlfilepath():
    # Get the current directory of the application
    current_dir = os.path.dirname(os.path.abspath(__file__))
    current_dir = current_dir + "\Asset\File"
    # Construct the file path
    file_name = "Trades executed at NSE.eml"  # Replace with your file name
    file_path = os.path.join(current_dir, file_name)

    print(file_path)
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            print("File Content:")
            print(content)
    except FileNotFoundError:
        print(f"File '{file_name}' not found in the application folder.")
    
    attributes = "amount, codinate"
    inputtext = "get " + attributes + "from" + "'" + content + "'"
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(inputtext)
    return jsonify({"data": response.text})


# Add a new item
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.json
    data.append(new_item)
    return jsonify(new_item), 201


@app.route('/upload-eml', methods=['POST'])
def upload_eml():
    # Get the uploaded file
    uploaded_file = request.files.get('file')
    input_data = request.form.get('inputData')

    if not uploaded_file or not input_data:
        return jsonify({"error": "File or input data is missing"}), 400

    # Save the file (optional)
    file_path = f"./uploads/{uploaded_file.filename}"
    uploaded_file.save(file_path)
    fileBodyContent = read_email_body(file_path)
    result = getDataFromGemini(fileBodyContent, input_data)

    return jsonify({"data": result})

def read_email_body(file_path):
    try:
        # Open the .eml file in binary mode
        with open(file_path, 'rb') as eml_file:
            # Parse the .eml file
            msg = BytesParser(policy=policy.default).parse(eml_file)

        # Extract the email body
        if msg.is_multipart():
            # If the email has multiple parts, get the plain text part
            for part in msg.iter_parts():
                if part.get_content_type() == "text/plain":
                    return part.get_content()
        else:
            # If the email is not multipart, return the content directly
            return msg.get_content()

    except FileNotFoundError:
        return f"File '{file_path}' not found."
    except Exception as e:
        return f"An error occurred: {str(e)}"
    

def getDataFromGemini(content, attributes):
    inputtext = "get " + attributes + "from" + "'" + content + "'"
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(inputtext)
    return response.text

# Run the app
if __name__ == '__main__':
    app.run(debug=True)