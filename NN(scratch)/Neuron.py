import random
import math

class Perceptron:

    def __init__(self , in_features):
        self.w = [random.uniform(-1 , 1) for _ in range(in_features)] # Weights
        self.b = random.uniform(-1 , 1) # Biases

    def __call__(self , x):
        out = sum([wi * xi for wi , xi in zip(self.w , x)] , self.b)
        out = 1 / (1 + math.exp(-out)) # Sigmoid
        return out