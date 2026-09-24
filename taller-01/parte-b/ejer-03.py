from concurrent.futures import ThreadPoolExecutor


def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print(e)


with ThreadPoolExecutor() as pool:
    futuro = pool.submit(dividir, 1, 0)
    futuro.result()

print("Listo")
