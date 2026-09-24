import multiprocessing
import threading

contador = 0


def incrementar() -> None:
    global contador
    contador += 1


if __name__ == "__main__":
    hilo = threading.Thread(target=incrementar)
    hilo.start()
    hilo.join()
    print("tras el hilo:   ", contador)

    proceso = multiprocessing.Process(target=incrementar)
    proceso.start()
    proceso.join()
    print("tras el proceso:", contador)
