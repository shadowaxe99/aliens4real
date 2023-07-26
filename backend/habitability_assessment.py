```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class HabitabilityAssessment:
    def __init__(self, exoplanet_data):
        self.exoplanet_data = pd.read_csv(exoplanet_data)
        self.model = RandomForestClassifier()

    def preprocess_data(self):
        self.exoplanet_data.dropna(inplace=True)
        self.exoplanet_data = pd.get_dummies(self.exoplanet_data)
        self.labels = self.exoplanet_data['Habitable']
        self.features = self.exoplanet_data.drop('Habitable', axis=1)

    def train_model(self):
        X_train, X_test, y_train, y_test = train_test_split(self.features, self.labels, test_size=0.2)
        self.model.fit(X_train, y_train)
        predictions = self.model.predict(X_test)
        print(f"Model Accuracy: {accuracy_score(y_test, predictions)}")

    def assess_habitability(self, exoplanet_features):
        prediction = self.model.predict([exoplanet_features])
        return prediction[0]

if __name__ == "__main__":
    habitability_assessment = HabitabilityAssessment('exoplanet_data.csv')
    habitability_assessment.preprocess_data()
    habitability_assessment.train_model()
    print(habitability_assessment.assess_habitability([1.0, 300, 0.7, 1.5, 0.8, 0.6, 0.4, 0.2, 0.1]))
```