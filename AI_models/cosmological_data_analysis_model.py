```python
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class CosmologicalDataAnalysisModel:
    def __init__(self):
        self.model = self.build_model()

    def build_model(self):
        model = keras.Sequential([
            layers.Dense(64, activation='relu', input_shape=[len(cosmologicalData.keys())]),
            layers.Dense(64, activation='relu'),
            layers.Dense(1)
        ])

        optimizer = tf.keras.optimizers.RMSprop(0.001)

        model.compile(loss='mse',
                      optimizer=optimizer,
                      metrics=['mae', 'mse'])
        return model

    def train_model(self, cosmologicalData, epochs=1000):
        X = cosmologicalData.drop('target', axis=1)
        y = cosmologicalData['target']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        scaler = StandardScaler()
        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        history = self.model.fit(
            X_train, y_train,
            epochs=epochs, validation_split=0.2, verbose=0)

        return history

    def predict(self, new_data):
        return self.model.predict(new_data)
```