# Twitter US Airline Sentiment Prediction

## Introduction
This project predicts sentiment (positive, negative, neutral) of tweets about US airlines using machine learning. The dataset includes 14,000+ tweets.

## Table of Contents
- Introduction
- Requirements
- Project Structure
- Getting Started
- Data
- Training
- Testing
- Evaluation
- Results
- Conclusion
- Author

## Requirements
- Python (3.6+)
- Jupyter Notebook
- pandas
- scikit-learn
- nltk
- numpy

## Project Structure
- data/
  - 0000000000002747_training_twitter_x_y_train.csv
  - 0000000000002747_test_twitter_x_test.csv
- notebooks/
  - twitter.ipynb
- README.md

## Getting Started
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Open 'twitter.ipynb' in the 'notebooks' directory using Jupyter Notebook.

## Data
The dataset contains training and test CSV files with tweet text and sentiment labels.

## Training
Preprocessing includes TF-IDF vectorization. A machine learning model (e.g., Random Forest) is trained on processed data.

## Testing
The trained model predicts sentiments for test data and saves predictions in a CSV file.

## Evaluation
Model performance is evaluated with accuracy, precision, recall, and F1-score metrics.

## Results
Notebook showcases evaluation metrics and test dataset predictions.

## Conclusion
Demonstrates text preprocessing, sentiment prediction model building, and evaluation. Illustrates ML's role in text sentiment classification.

## Author
Pradhyumn
