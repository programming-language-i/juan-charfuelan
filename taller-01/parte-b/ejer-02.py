import threading
import time


def guardar():
    try:
        time.sleep(2)
        print("guardado")
    finally:
        print("archivo cerrado")


threading.Thread(target=guardar, daemon=True).start()
print("Final")
