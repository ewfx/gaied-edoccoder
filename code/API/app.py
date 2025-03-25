from flask import Flask, jsonify, request
import requests
import time
import hmac
import hashlib
import base64
import json
import pathlib
import textwrap
import os
import google.generativeai as genai
from IPython.display import Markdown
from IPython.display import display

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
inputtext = "get amout, codinate and sulata from 'hi sulata amount : 50. sulata :satish codinate 90'"
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
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
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

    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(inputtext)
    return jsonify({"data": response.text})


# Add a new item
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.json
    data.append(new_item)
    return jsonify(new_item), 201

# Run the app
if __name__ == '__main__':
    app.run(debug=True)