```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class ExoplanetDetection:
    def __init__(self, data_file):
        self.data_file = data_file
        self.model = RandomForestClassifier()

    def load_data(self):
        self.data = pd.read_csv(self.data_file)
        self.features = self.data.drop('is_exoplanet', axis=1)
        self.labels = self.data['is_exoplanet']

    def train_model(self):
        X_train, X_test, y_train, y_test = train_test_split(self.features, self.labels, test_size=0.2, random_state=42)
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        print(f"Model Accuracy: {accuracy_score(y_test, predictions)}")

    def detect_exoplanets(self, new_data):
        self.load_data()
        self.train_model()
        predictions = self.model.predict(new_data)
        return predictions

if __name__ == "__main__":
    exoplanet_detector = ExoplanetDetection('cosmologicalData.csv')
    new_data = pd.read_csv('new_cosmologicalData.csv')
    exoplanet_predictions = exoplanet_detector.detect_exoplanets(new_data)
    print(f"Exoplanet Predictions: {exoplanet_predictions}")
```