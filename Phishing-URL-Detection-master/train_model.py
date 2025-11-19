import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load your dataset (adjust path and method)
df_train = pd.read_csv('your_training_data.csv')

# Drop the unwanted feature (replace 'feature_to_remove' with actual column name)
df_train = df_train.drop(columns=['feature_to_remove'])

# Separate features and target
X_train = df_train.drop(columns=['label'])
y_train = df_train['label']

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the trained model
with open('model_30features.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved with 30 features.")
