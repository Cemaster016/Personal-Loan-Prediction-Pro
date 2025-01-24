from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np
import joblib
import pandas as pd

app = Flask(__name__)

# Load the preprocessor and model
model = joblib.load("model.pkl")
preprocessor = joblib.load("preprocessor.pkl")

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Collect input from the form
        input_data = {
            'Age': float(request.form['Age']),
            'Experience': float(request.form['Experience']),
            'Income': float(request.form['Income']),
            'Family': int(request.form['Family']),
            'CCAvg': float(request.form['CCAvg']),
            'Education': int(request.form['Education']),
            'Mortgage': float(request.form['Mortgage']),
            'Securities_Account': int(request.form['Securities_Account']),
            'CD_Account': int(request.form['CD_Account']),
            'Online': int(request.form['Online']),
            'CreditCard': int(request.form['CreditCard']),
        }

        # Add the engineered features
        input_data['Income_per_Family'] = input_data['Income'] / (input_data['Family'] + 1e-5)
        input_data['Mortgage_to_Income'] = input_data['Mortgage'] / (input_data['Income'] + 1e-5)

        # Categorize Income into bins
        income_bins = [0, 50, 100, 150, float('inf')]
        income_labels = ['Low', 'Medium', 'High', 'Very High']
        input_data['Income_Category'] = pd.cut(
            [input_data['Income']],
            bins=income_bins,
            labels=income_labels
        )[0]  # Extract the single category value

        # Convert input to DataFrame for preprocessing
        input_df = pd.DataFrame([input_data])

        # Check for column mismatch with the preprocessor
        missing_cols = set(preprocessor.feature_names_in_) - set(input_df.columns)
        if missing_cols:
            raise ValueError(f"Missing columns in input data: {missing_cols}")

        # Apply the preprocessor to transform the input data
        transformed_input = preprocessor.transform(input_df)

        # Make prediction
        prediction = model.predict(transformed_input)[0]
        result = "Eligible for Loan" if prediction == 1 else "Not Eligible for Loan"

        return jsonify({'result': result})

    except Exception as e:
        error_message = f"Error: {str(e)}"
        return jsonify({'error': error_message}), 400

if __name__ == "__main__":
    app.run(debug=True)
