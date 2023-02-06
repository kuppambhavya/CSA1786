import numpy as np

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

def feed_forward(X, weights1, weights2):
  layer1 = sigmoid(np.dot(X, weights1))
  layer2 = sigmoid(np.dot(layer1, weights2))
  return layer2

if __name__ == "__main__":
  X = np.array([[1, 1, 1]])
  weights1 = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
  weights2 = np.array([[1, 1], [1, 1], [1, 1]])
  result = feed_forward(X, weights1, weights2)
  print(result)
