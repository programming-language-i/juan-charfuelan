import threading
import time
from tabulate import tabulate


# PRIMER HILO_______________________________________________________
def imprimir_mensaje1():
    for i in range(5):
        print(tabulate([["1: 90"]]))
        time.sleep(1)


# SEGUNDO HILO______________________________________________________
def imprimir_mensaje2():
    for i in range(5):
        print(tabulate([["2: 80"]]))
        time.sleep(2)


# TERCER HILO______________________________________________________
def imprimir_mensaje3():
    for i in range(5):
        print(tabulate([["3: 70"]]))
        time.sleep(3)


# CUARTO HILO______________________________________________________
def imprimir_mensaje4():
    for i in range(5):
        print(tabulate([["4: 60"]]))
        time.sleep(4)


# QUINTO HILO______________________________________________________
def imprimir_mensaje5():
    for i in range(5):
        print(tabulate([["5: 50"]]))
        time.sleep(5)


# SE CREAN LOS HILOS______________________________________________________
def main():
    thread1 = threading.Thread(target=imprimir_mensaje1)
    thread2 = threading.Thread(target=imprimir_mensaje2)
    thread3 = threading.Thread(target=imprimir_mensaje3)
    thread4 = threading.Thread(target=imprimir_mensaje4)
    thread5 = threading.Thread(target=imprimir_mensaje5)

    # SE INICIAN LOS HILOS______________________________________________________
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()

    # SE ESPERA A QUE TERMINEN LOS HILOS______________________________________________________
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()

    print("Finalizaron todos los hilos")


# EL EJECUTABLE___________________________________________________________
if __name__ == "__main__":
    main()
