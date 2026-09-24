import threading
import time


class Tarea(threading.Thread):
    def run(self):
        time.sleep(1)
        print(self.name, "lista")


inicio = time.perf_counter()
tareas = [Tarea(name=f"t{i}") for i in range(3)]

for t in tareas:
    t.start()

print(f"{time.perf_counter() - inicio:.1f} s")

for t in tareas:
    t.join()
