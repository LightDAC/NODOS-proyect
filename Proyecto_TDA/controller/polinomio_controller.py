from models.polinomio_model import PolinomioModel
from view.polinomio_view import PolinomioView

class PolinomioController:
    def __init__(self):
        self.v = PolinomioView()
    def crear(self):
        p = PolinomioModel()
        d = self.v.pedir("Términos exp:coef, ").split(",")
        for x in d:
            if ":" in x:
                e, c = x.split(":")
                p.agregar(int(e), float(c))
        return p
    def menu(self):
        while True:
            print("\n===== TDA POLINOMIO =====")
            print("1. Restar")
            print("2. Dividir")
            print("3. Eliminar")
            print("4. Existe")
            print("5. Volver")
            op = self.v.pedir("Opción: ")
            if op == "1":
                p1 = self.crear()
                p2 = self.crear()
                self.v.mostrar(str(p1.restar(p2)))
            elif op == "2":
                p1 = self.crear()
                p2 = self.crear()
                q, r = p1.dividir(p2)
                self.v.mostrar(str(q))
                self.v.mostrar(str(r))
            elif op == "3":
                p = self.crear()
                e = int(self.v.pedir("Exp: "))
                p.eliminar(e)
                self.v.mostrar(str(p))
            elif op == "4":
                p = self.crear()
                e = int(self.v.pedir("Exp: "))
                self.v.mostrar(str(p.existe(e)))
            elif op == "5":
                break
