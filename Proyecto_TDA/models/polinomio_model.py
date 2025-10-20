class PolinomioModel:
    def __init__(self):
        self.t = {}
    def agregar(self, e, c):
        self.t[e] = c
    def restar(self, otro):
        r = PolinomioModel()
        for e in self.t:
            r.t[e] = self.t[e] - otro.t.get(e, 0)
        return r
    def dividir(self, otro):
        if not otro.t:
            return None, None
        q = PolinomioModel()
        r = PolinomioModel()
        r.t = dict(self.t)
        e1 = max(self.t) if self.t else 0
        e2 = max(otro.t)
        while r.t and max(r.t) >= e2:
            exp = max(r.t) - e2
            co = r.t[max(r.t)] / otro.t[e2]
            q.t[exp] = co
            for k, v in otro.t.items():
                r.t[k + exp] = r.t.get(k + exp, 0) - v * co
            r.t = {k: v for k, v in r.t.items() if abs(v) > 1e-6}
        return q, r
    def eliminar(self, e):
        if e in self.t:
            del self.t[e]
    def existe(self, e):
        return e in self.t
    def __str__(self):
        return " + ".join([f"{v}x^{k}" for k, v in self.t.items()]) if self.t else "0"
