# 📰 Fake News Detection App
A simple end-to-end Machine Learning project that detects whether a news article or headline is Fake or Real using a Logistic Regression model.
The model is wrapped in a user-friendly Streamlit web app that allows anyone to test news articles live.

## 📊 Dataset

We used the [Fake and Real News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset).  
Please download it manually and place it in the `dataset/` folder.

## 🚀 Features
✅ Binary text classification (Fake vs. Real news)

🧠 Trained model using TF-IDF + Logistic Regression

🖥️ Streamlit web app with instant predictions

💾 Pickle files to save/load model & vectorizer

⚠️ Clear alerts when fake news is detected

## 📝 How to Use
1. Paste a news headline or article into the text box.

2. Click "Check News."

3. The app will instantly tell you if it's likely Fake or Real.

## 🚀 Future Improvements
* Add support for headline-only detection mode.
* Explore advanced NLP models (e.g., BERT, RoBERTa).
* Deploy online via Streamlit Cloud or Hugging Face Spaces.
