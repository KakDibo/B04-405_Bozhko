letters = 'abcdefghijklmnopqrstuvwxyz'

class N:
    def __init__(self):
        self.ch = {}
        self.p = None
        self.out = None

class T:
    def __init__(self):
        self.r = N()

    def add(self, s):
        cur = self.r
        for c in s:
            if c in cur.ch:
                cur = cur.ch[c]
            else:
                new_n = N()
                new_n.p = cur
                cur.ch[c] = new_n
                cur = new_n
        cur.out = s
    
    def find(self, w):
        cur = self.r
        for c in w:
            if c in cur.ch:
                cur = cur.ch[c]
            else:
                return False
        return cur.out == w
        
    def remove(self, w):
        cur = self.r
        for c in w:
            if c not in cur.ch:
                return
            cur = cur.ch[c]

        if cur.out != w:
            return
            
        cur.out = None
        
        while cur != self.r and not cur.ch and cur.out is None:
            parent = cur.p
            for k, v in parent.ch.items():
                if v is cur:
                    del parent.ch[k]
                    break
            cur = parent