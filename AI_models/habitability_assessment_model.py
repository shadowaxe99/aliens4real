```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class HabitabilityModel:
    def __init__(self, exoplanet_data):
        self.exoplanet_data = exoplanet_data
        self.model = self.build_model()

    def preprocess_data(self):
        # Extract features and target variable from exoplanet_data
        features = self.exoplanet_data.drop('habitable', axis=1)
        target = self.exoplanet_data['habitable']

        # Normalize features
        scaler = StandardScaler()
        features = scaler.fit_transform(features)

        # Split data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

        return X_train, X_test, y_train, y_test

    def build_model(self):
        # Define model architecture
        model = keras.Sequential([
            layers.Dense(64, activation='relu', input_shape=[len(self.exoplanet_data.columns)-1]),
            layers.Dense(64, activation='relu'),
            layers.Dense(1, activation='sigmoid')
        ])

        # Compile the model
        model.compile(loss='binary_crossentropy',
                      optimizer='adam',
                      metrics=['accuracy'])

        return model

    def train_model(self):
        X_train, X_test, y_train, y_test = self.preprocess_data()

        # Train the model
        history = self.model.fit(X_train, y_train,
                                 validation_data=(X_test, y_test),
                                 epochs=100, batch_size=10)

        return history

    def assess_habitability(self, exoplanet_features):
        # Normalize exoplanet_features
        scaler = StandardScaler()
        exoplanet_features = scaler.fit_transform(exoplanet_features)

        # Predict habitability
        habitability_prediction = self.model.predict(exoplanet_features)

        return habitability_prediction
```