import streamlit as st
import os
import time
from cnnClassifier.pipeline.prediction import PredictionPipeline

# Set environment variables for encoding
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

# Initialize the classifier
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"
        self.classifier = PredictionPipeline(self.filename)

clApp = ClientApp()

# Streamlit Page Config
st.set_page_config(page_title="🩺 COVID-19 Classifier", page_icon="🧬", layout="centered")

# -------------------------------
# Title Section
# -------------------------------
st.title("🩺 COVID-19 Detection")
st.markdown("""
This app uses a deep learning model to detect **covid-positive** and **covid-negative** chest X-rays.  
Upload an image and get predictions instantly.
""")

# -------------------------------
# Image Upload
# -------------------------------
st.subheader("📤 Upload Chest X-ray Image")
uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Save uploaded image
    with open(clApp.filename, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.image(clApp.filename, caption="🖼 Uploaded Image", use_column_width=True)
    st.write("")

    # Predict Button
    if st.button("🔍 Predict"):
        with st.spinner("Running model inference... please wait ⏳"):
            time.sleep(1)  # Simulate short delay
            result = clApp.classifier.predict()

        # Handle prediction output
        if isinstance(result, dict):
            # e.g., {"positive": 0.85, "negative": 0.15}
            st.success("### ✅ Prediction Complete!")
            predicted_label = max(result, key=result.get)
            st.write(f"### 🧠 Model Prediction: **{predicted_label.upper()}**")

            # Plot probabilities
            st.subheader("📊 Confidence Scores")
            st.bar_chart(result)
        else:
            # If the model returns only a label
            st.success(f"### ✅ Prediction Result: **{result}**")

# -------------------------------
# Training Section
# -------------------------------
st.write("---")
st.subheader("🧠 Retrain Model (Optional)")
st.markdown("""
If you've updated the dataset or model code, click below to re-run **DVC training pipeline**.
""")

if st.button("🚀 Run Training"):
    with st.spinner("Training model... this may take several minutes ⏱"):
        progress_text = "Running DVC pipeline..."
        progress_bar = st.progress(0)
        for percent_complete in range(0, 101, 10):
            time.sleep(0.3)
            progress_bar.progress(percent_complete)
        os.system("dvc repro")
    st.success("🎉 Training completed successfully!")

# -------------------------------
# Footer
# -------------------------------
st.write("---")
st.markdown("""
💡 **Tip:** Use high-quality chest X-rays for best accuracy.  
Made with ❤️ using Streamlit and your trained CNN model.
""")
