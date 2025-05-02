import streamlit as st
import pickle

# Load the model and vectorizer
with open('fake_news_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('tfidf_vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

# Streamlit app
st.title("📰 Fake News Detector")
st.subheader("Enter a news article or headline:")

# Text input
user_input = st.text_area("Paste your news text here...")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Transform input
        input_vect = vectorizer.transform([user_input])

        # Predict
        prediction = model.predict(input_vect)[0]

        # Display result
        if prediction == 1:
            st.success("✅ This news looks **Real**.")
        else:
            st.error("🚨 This news seems to be **Fake**.")
