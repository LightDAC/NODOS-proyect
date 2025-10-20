from models.calendario_model import CalendarioModel
from view.calendario_view import CalendarioView

class CalendarioController:
    def __init__(self):
        self.v = CalendarioView()
        self.m = CalendarioModel()
    def menu(self):
        while True:
            print("\n===== TDA CALENDARIO =====")
            print("1. Día actual")
            print("2. Pesca")
            print("3. Volver")
            op = self.v.pedir("Opción: ")
            if op == "1":
                d, w = self.m.hoy()
                self.v.mostrar(f"{d} {w}")
            elif op == "2":
                for x in self.m.pesca():
                    self.v.mostrar(str(x))
            elif op == "3":
                break
