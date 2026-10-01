import threading


def dividir(a: int, b: int) -> None:
    try:
        print(f"Resultado: {a / b}")
    except ZeroDivisionError as e:
        print(f"Error: i{e}")


hilo = threading.Thread(target=dividir, args=(5, 0))

hilo.start()
hilo.join()

print("Finalizar")
