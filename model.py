import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

data = pd.read_csv('HACKATHONS/WELLVISE/random_dataset.csv')

# Split the dataset into features (X) and target (y)
X = data[['QScore', 'Time_taken']].values
y = data['Cognitive_health_Score'].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(2,)),  # Input layer with 2 input features (QScore and Time_taken)
    tf.keras.layers.Dense(5, activation='relu'),  # Hidden layer with 5 nodes and ReLU activation
    tf.keras.layers.Dense(1)  # Output layer with 1 node
])

model.compile(optimizer='adam', loss='mean_squared_error')

batch_size = 32
epochs = 100
model.fit(X_train, y_train, batch_size=batch_size, epochs=epochs, validation_split=0.2)

test_loss = model.evaluate(X_test, y_test)
print(f"Test loss: {test_loss}")

model.save('HACKATHONS/WELLVISE/cognitive_health_model.h5')

print("Model trained and saved as 'cognitive_health_model.h5'.")
