📘 Phishing Website Detection Using Machine Learning

This project detects whether a given URL is legitimate or phishing using machine learning techniques.
It extracts various URL-based features, trains a model, and provides a user-friendly interface for predictions.

🚀 Features

✔️ Extracts 30+ features from URLs

✔️ Machine Learning model trained on phishing dataset

✔️ Flask-based web application for real-time prediction

✔️ Clean UI where user inputs any URL

✔️ Predicts "Legitimate" or "Phishing"

✔️ Can be extended to deploy online (Render / GitHub Pages / Railway)

🧠 Machine Learning Model

The pipeline includes:

Data preprocessing

Feature extraction (URL length, @ symbol use, SSL certificate, subdomains, etc.)

Model training using algorithms such as:

Random Forest

Decision Tree

Logistic Regression

The final model is saved as model.pkl for deployment.

📂 Project Structure
Phishing_website_detection/
│── app.py                 # Flask app for prediction UI
│── feature.py             # URL feature extraction logic
│── train_model.py         # ML model training script
│── phishing.csv           # Dataset
│── pickle/
│   └── model.pkl          # Saved ML model
│── templates/
│   └── index.html         # Frontend UI
│── static/
│   └── styles.css         # CSS styling
│── requirements.txt       # Dependencies
│── README.md              # Project documentation

🖥️ How to Run Locally
1. Clone the repository
git clone https://github.com/poojaK853/Phishing_website_detection.git

2. Navigate into folder
cd Phishing_website_detection

3. Install dependencies
pip install -r requirements.txt

4. Run the Flask app
python app.py

5. Open in browser
http://127.0.0.1:5000

🌐 Deployment

You can deploy this project on:

Render

Railway

Heroku

Azure Web Apps

I can help you deploy it—just ask! 🚀

📊 Dataset

The dataset (phishing.csv) contains labeled URLs:

1 = Phishing

0 = Legitimate

You can add additional features or extend the dataset for improved accuracy.

🛠️ Technologies Used

Python

Flask

Pandas

Scikit-learn

HTML + CSS

Jupyter Notebook
