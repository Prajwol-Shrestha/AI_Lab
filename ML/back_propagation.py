# Import the required libraries
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

# Define the input and target data
input_data = [[0, 0], [0, 1], [1, 0], [1, 1]]
target_data = [0, 1, 1, 0]

# Create a multi-layer perceptron (MLP) classifier object
classifier = MLPClassifier(
    hidden_layer_sizes=(3,),  # Number of units in the hidden layer
    activation='logistic',    # Activation function for the neurons
    solver='sgd',             # Solver algorithm for weight optimization (stochastic gradient descent)
    learning_rate_init=0.1,   # Initial learning rate
    max_iter=1000             # Maximum number of iterations for training
)

# Train the classifier using the input and target data
classifier.fit(input_data, target_data)

# Define the test data
test_data = [[0, 0], [0, 1], [1, 0], [1, 1]]

# Use the trained classifier to predict the outputs for the test data
predictions = classifier.predict(test_data)

# Print the predictions
print(predictions)
