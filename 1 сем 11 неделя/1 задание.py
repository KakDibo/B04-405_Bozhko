import unittest

def f(n, d = []):
    if n == 1:
        return d
    
    for i in range(2,n):
        if n % i == 0:
            d.append(i)
            return f(n//i, d)
        
    d.append(n)
    return d

class T(unittest.TestCase):
    def test_f(self):
        self.assertEqual(f(1), [1])
        self.assertEqual(f(2), [2])
        self.assertEqual(f(4), [2,2])
        self.assertEqual(f(0), [])

unittest.main()