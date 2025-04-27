import numpy as np
import unittest

def f(x, y):
    x, y = np.array(x), np.array(y)

    if len(x) < 2 or len(x) != len(y) or np.all(x == x[0]): 
        return None
    
    b = ((x*y).mean() - (x.mean() * y.mean())) / ((x**2).mean() - (x.mean())**2)
    a = y.mean() - b * x.mean()
    k = ((x*y).mean()) / ((x**2).mean())

    return [a, b, k]

x = [1, 2, 3, 4, 5]
y = [2, 3.2, 3.9, 4.5, 5.1]
print(f(x, y))


class T(unittest.TestCase):
    def test_t(self):
        self.assertTrue(isinstance(f([1, 2, 3], [1, 2, 3]),list))

    def test_n(self):
        self.assertIsNone(f([], []))

    def test_d(self):
        self.assertIsNone(f([1, 2, 3], [1, 2]))
        
    def test_s(self):
        self.assertIsNone(f([1, 1, 1], [1, 2, 3]))

unittest.main()