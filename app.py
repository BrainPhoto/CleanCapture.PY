import streamlit as st
import requests
from PIL import Image
import base64

# Azure Custom Vision API credentials
PREDICTION_KEY = "8f9ae3559303456a9297072314804f24"
URL_ENDPOINT_IMAGE = "https://brainphoto-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/de6d63d2-71eb-4309-acf3-50779f24bd0d/classify/iterations/Iteration2/image"
URL_ENDPOINT_URL = "https://brainphoto-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/de6d63d2-71eb-4309-acf3-50779f24bd0d/classify/iterations/Iteration2/url"

# Paths and URLs
image_path = "https://raw.githubusercontent.com/armaf002/CleanCapture/main/image/waste.png"
waste_app_url = "https://waste-chat.azurewebsites.net/"  # AI Chat Web App URL

# Sidebar navigation
st.sidebar.title("Waste Detection App")
menu = st.sidebar.radio("Navigate", ["Home", "Waste Upload", "Waste Capture", "Waste Streaming", "Recycling Guidelines", "AI Chat", "Feedback"])

# Home Page
if menu == "Home":
    response = requests.get(image_path)
    background_image = base64.b64encode(response.content).decode()

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
    
    # AI Chat Section
    st.markdown("""
        <div class='box'>
            <h2>🌟 Try Our AI Chat Assistant!</h2>
            <p>Have questions about waste management or recycling? Our AI chat assistant is here to help you! Click the button below to start chatting with our AI and get instant answers.</p>
            <a href='https://waste-chat.azurewebsites.net/' target='_blank'>
                <button style='background-color:#4CAF50; color:white; padding:15px 32px; text-align:center; text-decoration:none; display:inline-block; font-size:16px; border-radius:12px;'>Chat with AI</button>
            </a>
        </div>
    """, unsafe_allow_html=True)

# AI Chat Page
elif menu == "AI Chat":
    st.title("AI Chat Assistant")
    st.write("Have questions about waste management or recycling? Our AI chat assistant is here to help you!")
    st.write("Click the button below to start chatting with our AI and get instant answers.")

    # AI Chat Button
    st.markdown("""
        <a href='https://waste-chat.azurewebsites.net/' target='_blank'>
            <button style='background-color:#4CAF50; color:white; padding:15px 32px; text-align:center; text-decoration:none; display:inline-block; font-size:16px; border-radius:12px;'>Chat with AI</button>
        </a>
    """, unsafe_allow_html=True)

# Remaining code for Waste Upload, Capture, Streaming, Guidelines, and Feedback pages...
# Waste Upload Page
elif menu == "Waste Upload":
    st.title("Waste Upload")
    
    # Option to upload an image or use a URL
    upload_option = st.radio("Select Upload Option", ["Upload from File", "Upload from URL"])
    
    if upload_option == "Upload from File":
        image_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
        if image_file:
            image = Image.open(image_file)
            st.image(image, caption="Uploaded Image", use_column_width=True)

            # Send the image to Azure Custom Vision API
            headers = {
                "Prediction-Key": PREDICTION_KEY,
                "Content-Type": "application/octet-stream"
            }
            response = requests.post(URL_ENDPOINT_IMAGE, headers=headers, data=image_file.getvalue())
            prediction = response.json()
            
            # Displaying the results in a human-readable format
            st.write("### Prediction Results:")
            for pred in prediction["predictions"]:
                st.write(f"- **{pred['tagName']}**: {pred['probability'] * 100:.2f}%")

    elif upload_option == "Upload from URL":
        image_url = st.text_input("Enter Image URL")
        if image_url:
            headers = {
                "Prediction-Key": PREDICTION_KEY,
                "Content-Type": "application/json"
            }
            response = requests.post(URL_ENDPOINT_URL,
                                     headers=headers,
                                     json={"Url": image_url})
            prediction = response.json()
            st.image(image_url, caption="Image from URL", use_column_width=True)
            
            # Displaying the results in a human-readable format
            st.write("### Prediction Results:")
            for pred in prediction["predictions"]:
                st.write(f"- **{pred['tagName']}**: {pred['probability'] * 100:.2f}%")

# Waste Capture Page
elif menu == "Waste Capture":
    st.title("Waste Capture")
    st.write("This feature will allow you to capture an image live using your device's camera.")

    # Camera Capture (Streamlit built-in functionality)
    img_file_buffer = st.camera_input("Capture an image")
    if img_file_buffer:
        image = Image.open(img_file_buffer)
        st.image(image, caption="Captured Image", use_column_width=True)
        # Send captured image to Azure Custom Vision API
        headers = {
            "Prediction-Key": PREDICTION_KEY,
            "Content-Type": "application/octet-stream"
        }
        response = requests.post(URL_ENDPOINT_IMAGE, headers=headers, data=img_file_buffer.getvalue())
        prediction = response.json()
        
        # Displaying the results in a human-readable format
        st.write("### Prediction Results:")
        for pred in prediction["predictions"]:
            st.write(f"- **{pred['tagName']}**: {pred['probability'] * 100:.2f}%")

# Waste Streaming Page
elif menu == "Waste Streaming":
    st.title("Waste Streaming")
    st.write("This feature will allow you to stream video and capture frames for waste detection.")
    # Live streaming functionality (simplified)
    st.write("Feature in development.")

    # Streaming setup and processing will go here.

elif menu == "Recycling Guidelines":
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
    - **Handle Hazardous Waste Carefully:** Follow local guidelines for disposing of 
      hazardous materials.
    - **Reduce Waste:** Whenever possible, minimize the amount of non-recyclable 
      waste you produce by choosing reusable or recyclable alternatives.
    """)

# Feedback Page
elif menu == "Feedback":
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
            st.write(f"Message sent by **{name}** with subject **{subject}** successfully")
            st.success("Thank you for your feedback!")
