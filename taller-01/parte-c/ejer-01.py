import threading


class Descarga(threading.Thread):
    def __init__(self, archivo):
        super().__init__()
        self.archivo = archivo

    def run(self):
        print("descargar", self.archivo)


Descarga("a.zip").start()
