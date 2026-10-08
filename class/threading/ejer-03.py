import threading
import time

listo = False


def preparar() -> None:
    global listo
    time.sleep(1)
    listo = True


threading.Thread(target=preparar).start()
vueltas = 0
inicio = time.process_time()

while not listo:
    vueltas += 1
print(
    f"Espera activa: {vueltas:,} vueltas, {time.process_time() - inicio:.2f} s de CPU"
)

evento = threading.Event()


def preparar_evento() -> None:
    time.sleep(1)
    evento.set()


threading.Thread(target=preparar_evento).start()
inicio = time.process_time()
evento.wait()
print(f"Event.wait(): {time.process_time() - inicio:.2f} s de CPU")
