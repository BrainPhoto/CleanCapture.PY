import streamlit as st
import requests
import cv2
from PIL import Image
import numpy as np
import base64  

# Azure Custom Vision API details
prediction_url_file = "https://brainphoto-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/de6d63d2-71eb-4309-acf3-50779f24bd0d/classify/iterations/Iteration2/image"
prediction_url_url = "https://brainphoto-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/de6d63d2-71eb-4309-acf3-50779f24bd0d/classify/iterations/Iteration2/url"
prediction_key = "8f9ae3559303456a9297072314804f24"

# Function to send image to Azure Custom Vision API
def analyze_image(image):
    headers = {
        'Prediction-Key': prediction_key,
        'Content-Type': 'application/octet-stream'
    }
    response = requests.post(prediction_url_file, headers=headers, data=image)
    return response.json()

# Set up the main layout
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Live Streaming", "Capture Image", "Upload Image", "Recycling Guidelines", "Feedback"])

if page == "Home":
    # Inject CSS to set the background image
    with open("/workspaces/CleanCapture.PY/image/waste.png", "rb") as f:
        background_image = base64.b64encode(f.read()).decode()

    st.markdown(f"""
        <style>
        .stApp {{
            background-image: url('data:image/png;base64,{background_image}');
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .box {{
            background: rgba(255, 255, 255, 0.8);
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }}
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown("<div class='box'><h1>Welcome to the Recyclable Material Detector</h1><p>This app helps you detect organic and recyclable materials from images or live streaming. Navigate through the sidebar to explore the features.</p></div>", unsafe_allow_html=True)

elif page == "Live Streaming":
    st.title("Live Streaming")
    st.write("Analyze live video feed for recyclable objects.")
    # Live streaming functionality (simplified)
    st.write("Feature in development.")

elif page == "Capture Image":
    st.title("Capture Image")
    st.write("Capture an image using your device's camera and analyze it for recyclable materials.")
    captured_image = st.camera_input("Capture an image")

    if captured_image is not None:
        image = Image.open(captured_image)
        st.image(image, caption="Captured Image", use_column_width=True)

        # Convert image to bytes
        img_bytes = cv2.imencode('.jpg', np.array(image))[1].tobytes()

        # Send image to Azure Custom Vision API
        result = analyze_image(img_bytes)

        # Display results
        st.write("Prediction Results:")
        for prediction in result['predictions']:
            st.write(f"{prediction['tagName']}: {prediction['probability']*100:.2f}%")

elif page == "Upload Image":
    st.title("Upload Image")
    st.write("Upload an image file or provide an image URL to analyze it for recyclable materials.")
    upload_type = st.radio("Select upload type:", ["File Upload", "URL Upload"])

    if upload_type == "File Upload":
        uploaded_file = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)

            # Convert image to bytes
            img_bytes = uploaded_file.read()

            # Send image to Azure Custom Vision API
            result = analyze_image(img_bytes)

            # Display results
            st.write("Prediction Results:")
            for prediction in result['predictions']:
                st.write(f"{prediction['tagName']}: {prediction['probability']*100:.2f}%")

    else:
        image_url = st.text_input("Enter image URL")

        if image_url:
            # Send URL to Azure Custom Vision API
            headers = {
                'Prediction-Key': prediction_key,
                'Content-Type': 'application/json'
            }
            data = {"Url": image_url}
            response = requests.post(prediction_url_url, headers=headers, json=data)
            result = response.json()

            # Display image and results
            st.image(image_url, caption="Image from URL", use_column_width=True)
            st.write("Prediction Results:")
            for prediction in result['predictions']:
                st.write(f"{prediction['tagName']}: {prediction['probability']*100:.2f}%")

elif page == "Recycling Guidelines":
    st.title("Recycling Guidelines")
    st.write("""
    Welcome to the Recycling Guidelines page! Here, you'll find essential information 
    on how to categorize and dispose of different types of waste correctly. Proper 
    waste management is crucial for sustainability and environmental conservation. 
    Let's explore the guidelines for organic, recyclable, and non-recyclable waste.
    """)

    st.header("Organic Waste")
    st.write("""
    Organic waste consists of materials that come from living organisms and can 
    decompose naturally. Properly managing organic waste helps reduce landfill use 
    and promotes composting, which enriches the soil.
    """)
    st.subheader("Examples of Organic Waste:")
    st.write("""
    - Food scraps (e.g., vegetable peelings, fruit skins, meat, dairy)
    - Yard waste (e.g., grass clippings, leaves, branches)
    - Paper products (e.g., used paper towels, coffee filters, cardboard)
    - Animal waste (e.g., manure, pet droppings)
    """)

    st.subheader("How to Manage Organic Waste:")
    st.write("""
    - **Composting:** Collect organic waste in a compost bin to create nutrient-rich 
      compost for gardening.
    - **Municipal Organic Waste Programs:** Check if your local waste management 
      services provide organic waste collection.
    - **Avoid Contaminants:** Do not include non-compostable items like plastic or 
      metal in your organic waste.
    """)

    st.header("Recyclable Waste")
    st.write("""
    Recyclable waste includes materials that can be processed and used to create 
    new products. Proper sorting and recycling of these materials help reduce waste 
    in landfills and conserve natural resources.
    """)
    st.subheader("Examples of Recyclable Waste:")
    st.write("""
    - Paper (e.g., newspapers, magazines, office paper)
    - Cardboard (e.g., shipping boxes, cereal boxes)
    - Glass (e.g., bottles, jars)
    - Metals (e.g., aluminum cans, steel cans)
    - Plastics (e.g., bottles, containers, some packaging materials)
    - Electronics (e.g., old computers, phones, batteries)
    """)

    st.subheader("Recycling Tips:")
    st.write("""
    - **Clean Your Recyclables:** Rinse containers to remove food residue before recycling.
    - **Check Local Guidelines:** Recycling rules vary by region, so check your local 
      guidelines for accepted materials.
    - **Separate Materials:** Ensure that different types of materials are sorted 
      correctly (e.g., paper with paper, plastics with plastics).
    - **Avoid Contamination:** Do not mix non-recyclable items with recyclables, as 
      this can spoil the entire batch.
    """)

    st.header("Non-Recyclable Waste")
    st.write("""
    Non-recyclable waste includes items that cannot be easily processed or reused. 
    These materials should be disposed of in general waste bins.
    """)
    st.subheader("Examples of Non-Recyclable Waste:")
    st.write("""
    - Food-contaminated items (e.g., greasy pizza boxes, used napkins)
    - Certain plastics (e.g., plastic bags, styrofoam, some food packaging)
    - Ceramics and Pyrex (e.g., broken dishes, cups)
    - Non-recyclable paper (e.g., waxed paper, laminated paper)
    - Mixed-material items (e.g., chip bags, some types of packaging)
    - Hazardous waste (e.g., batteries, medical waste, chemicals)
    """)

    st.subheader("Proper Disposal of Non-Recyclable Waste:")
    st.write("""
    - **Dispose Safely:** Place non-recyclable waste in your regular trash bins.
    - **Handle Hazardous Waste Separately:** Items like batteries and chemicals should 
      be disposed of through special hazardous waste programs.
    - **Reduce Usage:** Minimize the use of non-recyclable materials where possible by 
      opting for reusable or recyclable alternatives.
    """)

    st.header("Additional Resources")
    st.write("""
    For more information on recycling guidelines specific to your region, visit the 
    following links:
    - [Recycling Guidelines by Region](#)
    - [How to Properly Dispose of Hazardous Materials](#)
    - [Tips on Reducing Waste and Promoting Sustainability](#)
    - [Composting at Home: A Beginner's Guide](#)
    """)

    st.write("""
    Remember, proper waste management starts with you! By following these guidelines, 
    you can contribute to a cleaner, more sustainable environment.
    """)

elif page == "Feedback":
    st.title("Feedback")
    st.write("Report any misclassifications or issues.")
    # st.write("Provide a way for users to report feedback, possibly via email.")
    
    with st.form(key='contact_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        subject = st.text_input("Subject")
        message = st.text_area("Message")
        submit_button = st.form_submit_button(label='Send')

        if submit_button:
            # You can replace this with your email sending logic
            st.write(f"Message sent by {name} with subject {subject}")

            