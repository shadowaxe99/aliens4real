```python
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
import pandas as pd

class StatisticalAnalysisModel:
    def __init__(self, data):
        self.data = data
        self.model = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None

    def preprocess_data(self):
        # Preprocessing the data
        self.data = self.data.dropna()

        # Splitting the data into features and target
        X = self.data.drop('LifeProbability', axis=1)
        y = self.data['LifeProbability']

        # Splitting the data into training and testing sets
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    def train_model(self):
        # Training the model
        self.model = RandomForestRegressor(n_estimators=100, random_state=42)
        self.model.fit(self.X_train, self.y_train)

    def evaluate_model(self):
        # Evaluating the model
        predictions = self.model.predict(self.X_test)
        mae = mean_absolute_error(self.y_test, predictions)
        return mae

    def predict_life_probability(self, input_data):
        # Predicting the probability of life
        prediction = self.model.predict(input_data)
        return prediction

if __name__ == "__main__":
    # Load data
    data = pd.read_csv('statisticalData.csv')

    # Initialize model
    model = StatisticalAnalysisModel(data)

    # Preprocess data
    model.preprocess_data()

    # Train model
    model.train_model()

    # Evaluate model
    mae = model.evaluate_model()
    print(f'Mean Absolute Error: {mae}')

    # Predict life probability
    input_data = np.array([[1, 2, 3, 4, 5]])  # example input data
    prediction = model.predict_life_probability(input_data)
    print(f'Predicted Life Probability: {prediction}')
```