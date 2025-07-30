# Question Label Formatter
This project is a machine learning-based classifier that standardizes raw question labels (such as "Q2", "3-a-i", or "The answer is below") into a canonical format (such as "2", "3(a)(i)", or "no_label"). It uses an SVM model with TF-IDF vectorization to recognize and classify text-based label variations. It also makes use of streamlit to create a clean website interface for users.

## Live Web App
Access the formatter here: https://label-formatter.streamlit.app/

## Features
- Classifies inconsistent labels into a neat, standard format.
- Learns from user corrections and adds new data automatically.
- Retains learning across sessions by saving updates to an Excel sheet.

## Technologies Used
- Python 3
- scikit-learn (SVM, TF-IDF)
- pandas
- openpyxl
- Streamlit (for the web interface)
- Excel (.xlsx) file as the training data backend

## Setup
### 1. Clone the Repository
- git clone https://github.com/adij296/label-SVM.git
  cd label-SVM
### 2. Install Dependencies
- pip install -r requirements.txt

## Running the Formatter
### Option A: Terminal/CLI Version
- Use the Label_SVM.py file to format a label via the terminal:
 python Label_SVM.py
- Enter in a raw label, and the Formatter will output the fortmatted label.
- If the model makes a mistake, you can correct it, and the new data will be saved and automatically added to the dataset for future learning.
- After multiple corrections are made, rerun the formatter for improved results.

### Option B: Streamlit Interface/Web App
- To launch the Streamlit interface locally:
 streamlit run streamlit_formatter.py
- Or open the live web app link above
- The formatter works the same way as described in Option A

## Important Notes
- Make sure the question_label_variations.xlsx file remains in the root or update the code paths accordingly.

- After making several corrections, restart the app or script to retrain the model with the new data.

- Use consistent formatting in the canonical_label column to preserve classifier accuracy.
