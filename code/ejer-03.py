import threading
import time


def latido() -> None:
    while True:
        print("latido")
        time.sleep(0.5)


# Uso de daemon
threading.Thread(target=latido, daemon=True).start()
time.sleep(2)
print("Terminar")
