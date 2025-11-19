
from flask import Flask, request, render_template
import numpy as np
import warnings
import pickle
warnings.filterwarnings('ignore')

from feature import FeatureExtraction  # your feature extraction code

# Load your model (adjust the path if needed)
with open("pickle/model.pkl", "rb") as file:
    gbc = pickle.load(file)

app = Flask(__name__)  # <- This line must be **before** @app.route



@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        
        # Extract features from the URL
        obj = FeatureExtraction(url)
        features = obj.getFeaturesList()
        print(f"Feature count before adjustment: {len(features)}")  # debug print
        
        # Ensure feature vector length matches model input
        required = 31
        if len(features) < required:
            features += [0] * (required - len(features))  # pad with zeros
        elif len(features) > required:
            features = features[:required]  # truncate if too long
        
        print(f"Feature count after adjustment: {len(features)}")  # debug print
        
        x = np.array(features).reshape(1, -1)  # reshape for model input
        
        # Predict
        y_pred = gbc.predict(x)[0]  # 1 means safe, -1 means unsafe
        
        y_pro_phishing = gbc.predict_proba(x)[0, 0]
        y_pro_non_phishing = gbc.predict_proba(x)[0, 1]
        
        # Prepare message for user
        pred = "It is {0:.2f}% safe to go".format(y_pro_phishing * 100)
        
        # Render template with probability of safe browsing
        return render_template('index.html', xx=round(y_pro_non_phishing, 2), url=url)
    
    # For GET requests
    return render_template("index.html", xx=-1)
if __name__ == "__main__":
    app.run(debug=True)

