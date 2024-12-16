def q(a):
    if len(a) <= 1:
        return a
    
    p = a[len(a)//2]
    l = list(set([x for x in a if x < p]))
    e = list(set([x for x in a if x == p]))
    m = list(set([x for x in a if x > p]))

    return q(l) + e + q(m)

s = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
print(q(s))

a = [2,2,2,2,2,2,2,2,2,2,2,2,2]
print(q(a))



class T(unittest.TestCase):
    def test_q(self):
        self.assertEqual(q([10,9,8,7,6,5,4,3,2,1]), sorted(list(set([10,9,8,7,6,5,4,3,2,1]))), "1")
        self.assertEqual(q([-10,6,-11,6, 55, 100]), sorted(list(set([-10,6,-11,6, 55, 100]))) , "3")


unittest.main()