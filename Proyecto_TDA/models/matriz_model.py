import random
class MatrizModel:
    def __init__(self, n):
        self.n = n
        self.m = [[0]*n for _ in range(n)]
    def aleatoria(self):
        self.m = [[random.randint(0, 9) for _ in range(self.n)] for _ in range(self.n)]
    def sumar(self, o):
        r = MatrizModel(self.n)
        for i in range(self.n):
            for j in range(self.n):
                r.m[i][j] = self.m[i][j] + o.m[i][j]
        return r
    def restar(self, o):
        r = MatrizModel(self.n)
        for i in range(self.n):
            for j in range(self.n):
                r.m[i][j] = self.m[i][j] - o.m[i][j]
        return r
    def mult(self, o):
        r = MatrizModel(self.n)
        for i in range(self.n):
            for j in range(self.n):
                for k in range(self.n):
                    r.m[i][j] += self.m[i][k] * o.m[k][j]
        return r
    def __str__(self):
        return "\n".join([" ".join(map(str, fila)) for fila in self.m])
