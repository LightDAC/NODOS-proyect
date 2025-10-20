from models.archivos_model import ArchivosModel
from view.archivos_view import ArchivosView

class ArchivosController:
    def __init__(self):
        self.v = ArchivosView()
        self.m = ArchivosModel()
    def menu(self):
        self.m.abrir()
        while True:
            print("\n===== TDA ARCHIVOS =====")
            print("1. Guardar")
            print("2. Leer")
            print("3. Modificar")
            print("4. Volver")
            op = self.v.pedir("Opción: ")
            if op == "1":
                c = self.v.pedir("Clave: ")
                d = self.v.pedir("Dato: ")
                self.m.guardar(c, d)
            elif op == "2":
                c = self.v.pedir("Clave: ")
                self.v.mostrar(str(self.m.leer(c)))
            elif op == "3":
                c = self.v.pedir("Clave: ")
                d = self.v.pedir("Nuevo dato: ")
                self.m.modificar(c, d)
            elif op == "4":
                self.m.cerrar()
                break
