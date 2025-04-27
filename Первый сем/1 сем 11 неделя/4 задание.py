import unittest
class C:
    a = "яюэьыъщшчцхфутсрпонмлкйизжёедгвба"

    def __init__(self, k):
        self._e = {}
        self._d = {}
        for i in range(len(self.a)):
            l = self.a[i]
            c = self.a[(i + k) % len(self.a)]
            self._e[l] = c
            self._e[l.upper()] = c.upper()
            self._d[c] = l
            self._d[c.upper()] = l.upper()

    def en(self, t):
        return ''.join([self._e.get(ch, ch) for ch in t])

    def de(self, t):
        return ''.join([self._d.get(ch, ch) for ch in t])


class T(unittest.TestCase):
    def test_el(self):
        c = C(3)
        self.assertEqual(c.en("абв"), "где")

    def test_eu(self):
        c = C(3)
        self.assertEqual(c.en("АБВ"), "ГДЕ")

    def test_en(self):
        c = C(3)
        self.assertEqual(c.en("абв123"), "где123")

    def test_dl(self):
        c = C(3)
        self.assertEqual(c.de("где"), "абв")

    def test_du(self):
        c = C(3)
        self.assertEqual(c.de("ГДЕ"), "АБВ")

    def test_dn(self):
        c = C(3)
        self.assertEqual(c.de("где123"), "абв123")

unittest.main()