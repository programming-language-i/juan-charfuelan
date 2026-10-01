import threading


def dividir(a: int, b: int) -> None:
    print(f"Resultado: {a / b}")


hilo = threading.Thread(target=dividir, args=(5, 0))

hilo.start()
hilo.join()

print("Finalizar")
