import os
import pickle  
from flask import Flask, request, jsonify, render_template


app = Flask(__name__)


try:
    with open("svm_twitter_sentiment.pkl", "rb") as f:
        model = pickle.load(f)
except FileNotFoundError as e:
    print(f"Error loading model: {e}")
    exit(1)


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
        prediction = model.predict([tweet])[0]

        # Return prediction as JSON response
        response = {
            "prediction": prediction,
        }
        return jsonify(response)

    except Exception as e:  # Catch generic errors
        print(f"Error during prediction: {e}")
        return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5050)
