# Import the scikit-learn module for machine learning
import sklearn
import numpy as np

# Load the dataset of tic-tac-toe games
dataset = np.load("tic-tac-toe-data.data", dtype=str)

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(
    dataset.data, dataset.target, test_size=0.25, random_state=0
)

# Create a machine learning model using the decision tree algorithm
model = sklearn.tree.DecisionTreeClassifier()

# Train the model using the training set
model.fit(X_train, y_train)

# Evaluate the model using the test set
accuracy = model.score(X_test, y_test)
print("Model accuracy:", accuracy)

# Save the trained model to a file
sklearn.dump(model, "tic-tac-toe-model.data")
