import csv
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# File path for CSV data
CSV_FILE_PATH = "svm_model_output.csv"

# Function to load data from CSV file
def load_data_from_csv():
    data = []
    try:
        with open(CSV_FILE_PATH, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        print(f"CSV file '{CSV_FILE_PATH}' not found.")
    return data

# Load data from CSV file on startup
sentiment_data = load_data_from_csv()

@app.route("/", methods=["GET"])
def index():
    """Serves the HTML template for the sentiment analysis interface."""
    return render_template("my.html")

@app.route("/predict", methods=["POST"])
def predict():
    """Predicts sentiment based on the provided tweet in the request body."""
    try:
        # Extract tweet from request data
        tweet = request.json["tweet"]

        # Make prediction using the loaded model
        # Here you would typically use a machine learning model for prediction,
        # but for this example, let's assume it's a simple check against CSV data
        sentiment = None
        for row in sentiment_data:
            if row["tweet"] == tweet:
                sentiment = row["sentiment"]
                break

        if sentiment:
            response = {"prediction": sentiment}
            return jsonify(response)
        else:
            return jsonify({"error": "Sentiment not found"}), 404

    except Exception as e:  # Catch generic errors
        print(f"Error during prediction: {e}")
        return jsonify({"error": "Internal server error"}), 500

@app.route("/reset", methods=["GET"])
def reset():
    """Resets the input field."""
    return render_template("my.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050)
