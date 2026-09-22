import threading
import time


def latido() -> None:
    while True:
        print("latido")
        time.sleep(0.5)


threading.Thread(target=latido, daemon=True).start()
time.sleep(2)
print("Terminar")
