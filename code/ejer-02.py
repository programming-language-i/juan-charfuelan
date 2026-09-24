import threading
import random
import time


class Sensor(threading.Thread):
    def __init__(self, nombre: str, ciclos: int) -> None:
        super().__init__(name=nombre)
        self.ciclos = ciclos
        self.lecturas: list[float] = []

    def run(self) -> None:
        for _ in range(self.ciclos):
            time.sleep(random.uniform(0.1, 0.3))
            self.lecturas.append(round(random.uniform(15, 30), 1))


sensores = [Sensor(nombre, 3) for nombre in ("temperatura", "humedad")]

for sensor in sensores:
    sensor.start()
for sensor in sensores:
    sensor.join()
for sensor in sensores:
    print(sensor.name, sensor.lecturas)  # cada uno con sus propias lecturas
