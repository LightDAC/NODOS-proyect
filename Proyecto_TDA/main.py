from controller.archivos_controller import ArchivosController
from controller.calendario_controller import CalendarioController
from controller.polinomio_controller import PolinomioController
from controller.matriz_controller import MatrizController

def main():
    while True:
        print("        MENÚ PRINCIPAL      ")
        print("1. TDA Archivos")
        print("2. TDA Calendario")
        print("3. TDA Polinomio")
        print("4. TDA Matriz")
        print("5. Salir")
        op = input("Opción: ")
        if op == "1":
            ArchivosController().menu()
        elif op == "2":
            CalendarioController().menu()
        elif op == "3":
            PolinomioController().menu()
        elif op == "4":
            MatrizController().menu()
        elif op == "5":
            print("Saliendo...")
            break

if __name__ == "__main__":
    main()
