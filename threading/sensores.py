import threading
import time


def sensor(nombre, temperatura):
    print(f"{nombre} empieza a medir la temperatura")

    for i in range(5):
        print(f"{nombre} - medición {i + 1}: {temperatura}°C")
        time.sleep(1)

    print(f"{nombre} terminado")


if __name__ == "__main__":
    threads = [
        threading.Thread(target=sensor, args=("Sensor 1", 30)),
        threading.Thread(target=sensor, args=("Sensor 2", 40)),
        threading.Thread(target=sensor, args=("Sensor 3", 50)),
        threading.Thread(target=sensor, args=("Sensor 4", 90)),
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Todos los sensores terminaron")
