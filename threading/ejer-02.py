import threading

contador = 0
lock = threading.Lock()


def incrementar():
    global contador

    with lock:
        contador += 1


if __name__ == "__main__":
    hilos = []

    for _ in range(100):
        hilo = threading.Thread(target=incrementar)
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()

    print("contador:", contador)
