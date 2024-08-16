# Introduction
CleanCapture.PY is a web application developed with Streamlit, designed to capture and process images efficiently. This project uses popular Python libraries such as requests, Pillow, and numpy to provide image manipulation and display functionalities.

## Features
- **Image Capture**: Capture and display images directly from the web interface.
- **Image Processing**: Apply various transformations and filters to the captured images.
- **Save and Share**: Easily save and share the processed images.

## Prerequisites
Make sure you have installed the following before starting the project:
- Python 3.7+
- pip (Python package manager)

## Installation
Clone the GitHub repository to your local machine:
```bash
git clone https://github.com/BrainPhoto/CleanCapture.PY.git
cd CleanCapture.PY

Create a virtual environment (recommended) and activate it:

python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`

If the requirements.txt file does not exist yet, create it by adding the following dependencies:

streamlit
requests
Pillow
numpy

Run the Streamlit application:

streamlit run app.py

This will open your application in a web browser.

Usage
Access the application via your web browser.
Use the interface to capture images, apply filters, and save them.
Share the processed images directly from the application.
Project Structure

Project Structure

CleanCapture.PY/
│
├── app.py              # Main entry point of the Streamlit application
├── requirements.txt    # File listing the project dependencies
├── README.md           # This README file
├── assets/             # Folder containing images, logos, etc.