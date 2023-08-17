Twitter US Airline Sentiment Prediction

This project involves predicting the sentiment (positive, negative, or neutral) of tweets related to various US airlines. The dataset used for training and testing contains over 14,000 tweets.

Table of Contents:
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

Introduction:
The goal of this project is to build a machine learning model that can predict the sentiment of tweets related to US airlines. The sentiments can be categorized as positive, negative, or neutral. The project involves preprocessing the data, training the model, and evaluating its performance.

Requirements:
- Python (3.6 or later)
- Jupyter Notebook
- pandas
- scikit-learn
- nltk
- numpy

Project Structure:
The project's directory structure is organized as follows:

- data/
  - 0000000000002747_training_twitter_x_y_train.csv
  - 0000000000002747_test_twitter_x_test.csv
- notebooks/
  - twitter.ipynb
- README.txt

Getting Started:
1. Clone this repository.
2. Install the required dependencies using 'pip install -r requirements.txt'.
3. Open the Jupyter Notebook 'twitter.ipynb' in the 'notebooks' directory.

Data:
The dataset consists of two CSV files:
- '0000000000002747_training_twitter_x_y_train.csv': Contains training data with tweet text and corresponding sentiment labels.
- '0000000000002747_test_twitter_x_test.csv': Contains test data with tweet text for which we need to predict sentiments.

Training:
In the notebook, the training data is loaded and preprocessed. Various techniques like TF-IDF vectorization are applied to convert text data into numerical features. A machine learning model, such as a Random Forest Classifier, is trained on the preprocessed data.

Testing:
The trained model is used to predict sentiments for the test dataset. The predictions are saved in a CSV file without headers.

Evaluation:
The accuracy of the model is evaluated using appropriate metrics such as accuracy, precision, recall, and F1-score. These metrics provide insights into the model's performance.

Results:
The final results, including evaluation metrics and predictions for the test dataset, are presented in the notebook.

Conclusion:
This project demonstrates how to preprocess text data, build a sentiment prediction model, and evaluate its performance. It provides a practical example of how machine learning can be used to classify sentiments in text data.

Author:
Pradhyumn


