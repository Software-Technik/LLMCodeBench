import sys

def tokenize(s):
    s = s.replace("(", " ( ").replace(")", " ) ")
    tokens = []
    for t in s.split():
        if t in '()+*':
            tokens.append(t)
        else:
            tokens.append(int(t))
    return tokens

class Parser1:
    def __init__(self, tokens):
        self.t = tokens; self.i = 0
    def peek(self):
        return self.t[self.i] if self.i < len(self.t) else None
    def get(self):
        v = self.peek(); self.i += 1; return v
    def factor(self):
        c = self.get()
        if c == '(':
            v = self.expr()
            self.get()
            return v
        return c
    def expr(self):
        v = self.factor()
        while True:
            op = self.peek()
            if op in ('+', '*'):
                self.get()
                w = self.factor()
                v = v + w if op == '+' else v * w
            else:
                break
        return v

class Parser2:
    def __init__(self, tokens):
        self.t = tokens; self.i = 0
    def peek(self):
        return self.t[self.i] if self.i < len(self.t) else None
    def get(self):
        v = self.peek(); self.i += 1; return v
    def factor(self):
        c = self.get()
        if c == '(':
            v = self.expr()
            self.get()
            return v
        return c
    def sum(self):
        v = self.factor()
        while self.peek() == '+':
            self.get()
            v += self.factor()
        return v
    def expr(self):
        v = self.sum()
        while self.peek() == '*':
            self.get()
            v *= self.sum()
        return v

with open(sys.argv[1]) as f:
    lines = [l for l in f.read().splitlines() if l]

s1 = s2 = 0
for line in lines:
    tokens = tokenize(line)
    s1 += Parser1(tokens).expr()
    s2 += Parser2(tokens).expr()
print(s1, s2)