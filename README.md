# Introduction

**CleanCapture.PY** is a web application developed with Streamlit, designed to capture, classify, and process waste images efficiently. This project integrates with Azure Custom Vision for automated waste classification and includes an AI chat feature for interactive support. It leverages popular Python libraries such as requests, Pillow, and numpy to provide advanced image manipulation and display functionalities.

## Features

- **Waste Classification**: Automatically classify waste as organic, recyclable, or non-recyclable using Azure Custom Vision.
- **Image Capture**: Capture and display images directly from the web interface.
- **Image Upload**: Upload images of waste for classification.
- **Live Streaming**: Stream live video for real-time waste classification.
- **Recycling Guidelines**: Access educational content on proper waste disposal practices.
- **AI Chat**: Interact with an AI chatbot for waste management queries, deployed via Azure OpenAI.
- **Feedback**: Provide feedback on the application for continuous improvement.

## Prerequisites

Ensure you have the following installed before starting the project:

- Python 3.7+
- pip (Python package manager)
- Streamlit (install via `pip`)

## Installation

1. Clone the GitHub repository to your local machine:
    ```bash
    git clone https://github.com/BrainPhoto/CleanCapture.PY.git
    cd CleanCapture.PY
    ```

2. Create a virtual environment (recommended) and activate it:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

    If the `requirements.txt` file does not exist yet, create it by adding the following dependencies:
    ```
    streamlit
    requests
    Pillow
    numpy
    ```

4. Run the Streamlit application:
    ```bash
    streamlit run app.py
    ```

    This will open your application in a web browser.

## Usage

- **Access the application** via your web browser.
- **Use the interface** to capture images, upload them for classification, stream live video, and access recycling guidelines.
- **Interact with the AI Chat** feature for support on waste management.
- **Provide feedback** on the application to help us improve.

## Project Structure

```
CleanCapture.PY/
│
├── app.py              # Main entry point of the Streamlit application
├── requirements.txt    # File listing the project dependencies
├── README.md           # This README file
├── application_overview.md # Detailed overview of the application features
├── problem_research.md # Research and problem statement
├── solution_identification.md # Solution identification and features
├── solution_implementation.md # Implementation details and steps
├── image/              # Folder containing screenshots and images
│   ├── ai_chat1.png    # Screenshot of the AI Chat feature
│   ├── ai_chat2.png    # Additional screenshot of the AI Chat feature
│   ├── feedback.png    # Screenshot of the Feedback feature
│   ├── home.png        # Screenshot of the Home screen
│   ├── recycling_guideline.png # Screenshot of the Recycling Guidelines feature
│   ├── waste.png       # Screenshot of the Waste Upload feature
│   ├── waste_capture.png # Screenshot of the Waste Capture feature
│   ├── waste_streaming.png # Screenshot of the Waste Streaming feature
│   └── waste_upload.png # Screenshot of the Waste Upload feature

```
