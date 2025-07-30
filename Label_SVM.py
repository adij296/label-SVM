
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from openpyxl import load_workbook

# Load data from spreadsheet
excel_path = 'question_label_variations.xlsx'
data = pd.read_excel(excel_path)

# Assign labels
X = data['raw_label'].astype(str)         # e.g., "Q1", "question one"
y = data['canonical_label'].astype(str)   # ensure labels are strings

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Text vectorization with TF-IDF
vectorizer = TfidfVectorizer(analyzer='char_wb', ngram_range=(2, 4))
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train SVM
model = SVC(kernel='rbf', C=1.0, gamma='scale')
model.fit(X_train_tfidf, y_train)

# Get label input from user
while True:
    user_input = input("Enter a label (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        break

    #Predict canonical label
    user_input_tfidf = vectorizer.transform([user_input])
    prediction = model.predict(user_input_tfidf)
    print("Predicted canonical label:", prediction[0])
    
    feedback = input("Is this correct? (y/n): ")
    if feedback.lower() == "n":
        correct_label = input("Please enter the correct label: ")
        # Save corrected input for future training
        new_entry = [[user_input, correct_label]]
        wb = load_workbook(excel_path)
        ws = wb.active
        for row in new_entry:
            ws.append(row)
        wb.save(excel_path)

