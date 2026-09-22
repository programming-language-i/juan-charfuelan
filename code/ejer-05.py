import threading


def dividir(a: int, b: int) -> None:
    print(a / b)


hilo = threading.Thread(target=dividir, args=(1, 0))
hilo.start()
hilo.join()
print("el principal sigue")
