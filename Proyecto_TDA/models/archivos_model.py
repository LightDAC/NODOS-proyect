import shelve
class ArchivosModel:
    def __init__(self):
        self.db = None
    def abrir(self):
        self.db = shelve.open("datos")
    def guardar(self, clave, dato):
        self.db[clave] = dato
    def leer(self, clave):
        return self.db.get(clave, None)
    def modificar(self, clave, dato):
        if clave in self.db:
            self.db[clave] = dato
    def cerrar(self):
        if self.db:
            self.db.close()
