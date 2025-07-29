# Question Label Formatter
This project is a machine learning-based classifier that standardizes raw question labels (such as "Q2", "3-a-i", or "The answer is below") into a canonical format (such as "2", "3(a)(i)", or "no_label"). It uses an SVM model with TF-IDF vectorization to recognize and classify text-based label variations.

## Features
- Classifies inconsistent labels into a neat, standard format.
- Learns from user corrections and appends new data automatically.
- Retains learning across sessions by saving updates to an Excel sheet.

## Technologies Used
- Python 3
- scikit-learn (SVM, TF-IDF)
- pandas
- openpyxl
- Excel (.xlsx) file as the training data backend

## Running the Formatter
### 1. Install Dependencies
- pip install pandas scikit-learn openpyxl
### 2. Prepare the Dataset
- Ensure your Excel file (question_label_variations.xlsx) has two columns:
  - raw_label (ex. Q-2, 3-a-i, shown below, ...) 
  - canonical_label (ex. 2, 3(a)(i), no_label, ...)

- Place the file in the specified path (e.g., C:\\Users\\...\\Downloads\\question_label_variations.xlsx).

### 3. Run the Formatter
- Enter in a raw label, and the Formatter will output the fortmatted label.
- If the model makes a mistake, you can correct it, and the new data will be saved and automatically added to the dataset for future learning.
- After multiple corrections are made, rerun the formatter for improved results.
