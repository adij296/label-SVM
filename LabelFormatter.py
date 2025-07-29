import streamlit as st
import pandas as pd
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from openpyxl import load_workbook

# Load and prepare data
EXCEL_PATH = 'question_label_variations.xlsx'
data = pd.read_excel(EXCEL_PATH)
X = data['raw_label'].astype(str)
y = data['canonical_label'].astype(str)

# Vectorization
vectorizer = TfidfVectorizer(analyzer='char_wb', ngram_range=(2, 4))
X_tfidf = vectorizer.fit_transform(X)

# Train SVM model
model = SVC(kernel='rbf', C=1.0, gamma='scale')
model.fit(X_tfidf, y)

# Streamlit UI
st.title("Canonical Label Formatter")
st.write("Standardize unorganized question labels into a neat canonical form.")

user_input = st.text_input("Enter a label:", "")

if user_input:
    user_input_tfidf = vectorizer.transform([user_input])
    prediction = model.predict(user_input_tfidf)[0]
    st.write(f"**Predicted canonical label:** `{prediction}`")

    feedback = st.radio("Is this correct?", options=["", "Yes", "No"], index=0, format_func=lambda x: "" if x == "" else x)

    if feedback == "":
        st.warning("Please select Yes or No to proceed.")
    elif feedback == "Yes":
        st.success("Great! Prediction confirmed. Please enter another label.")
    elif feedback == "No":
        correct_label = st.text_input("Please enter the correct canonical label:")
        if correct_label:
            # Save the corrected label
            try:
                wb = load_workbook(EXCEL_PATH)
                ws = wb.active
                ws.append([user_input, correct_label])
                wb.save(EXCEL_PATH)
                st.success("Feedback saved and added to the dataset! Please enter another label.")
            except Exception as e:
                st.error(f"Error saving feedback: {e}")