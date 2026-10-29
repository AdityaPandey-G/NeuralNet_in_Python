import random
import math

class Percep:

    def __init__(self , in_features):
        self.w = [random.uniform(-1 , 1) for _ in range(in_features)]
        self.b = random.uniform(-1 , 1)

    def __call__(self , x):
        out = sum([wi * xi for wi , xi in zip(self.w , x)] , self.b)
        return out

x = [1 , 2 , 3 , 4 , 5]
n = Percep(len(x))
print(n(x))