import random, threading, time

conexiones = threading.Semaphore(3)
lock = threading.Lock()
activas = 0


def descargar(i: int) -> None:
    global activas

    with conexiones:
        with lock:
            activas += 1
            print(f"descarga {i} empieza, activas: {activas}")

        time.sleep(random.uniform(0.2, 0.5))

        with lock:
            activas -= 1
            print(f"descarga {i} termina, activas: {activas}")


hilos = [threading.Thread(target=descargar, args=(i,)) for i in range(10)]
for h in hilos:
    h.start()
for h in hilos:
    h.join()
