from models.matriz_model import MatrizModel
from view.matriz_view import MatrizView

class MatrizController:
    def __init__(self):
        self.v = MatrizView()
    def menu(self):
        while True:
            print("\n===== TDA MATRIZ =====")
            print("1. Crear")
            print("2. Sumar")
            print("3. Restar")
            print("4. Multiplicar")
            print("5. Volver")
            op = self.v.pedir("Opción: ")
            if op in ["1", "2", "3", "4"]:
                n = int(self.v.pedir("n: "))
                a = MatrizModel(n)
                b = MatrizModel(n)
                a.aleatoria()
                b.aleatoria()
                if op == "1":
                    self.v.mostrar(str(a))
                elif op == "2":
                    self.v.mostrar(str(a.sumar(b)))
                elif op == "3":
                    self.v.mostrar(str(a.restar(b)))
                elif op == "4":
                    self.v.mostrar(str(a.mult(b)))
            elif op == "5":
                break
