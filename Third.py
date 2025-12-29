# Import required libraries
import streamlit as st  # For creating web app
import numpy as np  # For numerical operations
import pandas as pd  # For data manipulation
from sklearn import datasets  # For loading iris dataset
from sklearn.ensemble import RandomForestClassifier  # ML model for classification

# Display app title and description
st.write("""
  
# Simple Iris Flower Prediction

This app predicts the Iris flower type!
    
""")

# Create sidebar header
st.sidebar.header('User Input Parameters')

# Function to get user input from sidebar sliders
def user_input_features():
    # Create sliders for each feature (min, max, default)
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    # Store values in dictionary
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    # Convert to DataFrame for model input
    features = pd.DataFrame(data, index=[0])
    return features

# Get user input
df = user_input_features()

# Display user input values
st.subheader('User Input parameters')
st.write(df)

# Load iris dataset
iris = datasets.load_iris()
X = iris.data  # Features (sepal/petal measurements)  # pylint: disable=no-member
Y = iris.target  # Labels (flower types: 0, 1, 2)  # pylint: disable=no-member

# Create and train the model
clf = RandomForestClassifier()
clf.fit(X, Y)  # Train on entire iris dataset

# Make predictions on user input
prediction = clf.predict(df)  # Predicted class (0, 1, or 2)
prediction_proba = clf.predict_proba(df)  # Probability for each class

# Display class labels
st.subheader('Class labels and their corresponding index number')
st.write(iris.target_names)  # ['setosa', 'versicolor', 'virginica']  # pylint: disable=no-member

# Display prediction result
st.subheader('Prediction')
st.write(iris.target_names[prediction])  # Show flower name  # pylint: disable=no-member

# Display prediction probabilities
st.subheader('Prediction Probability')
st.write(prediction_proba)  # Probability for each of the 3 classes
