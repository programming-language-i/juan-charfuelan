class Mensaje:
    def __init__(self, emisor: str, contenido: str, timestamp: str) -> None:
        self.emisor = emisor
        self.contenido = contenido
        self.timestamp = timestamp

    def a_json(self) -> str:
        return json.dumps(
            {"emisor": self.emisor, "contenido": self.contenido, "timestamp": self.timestamp},
            ensure_ascii=False,
        )

    @classmethod
    def desde_json(cls, texto: str) -> "Mensaje":
        datos = json.loads(texto)
        return cls(datos["emisor"], datos["contenido"], datos["timestamp"])

hola = Mesaje()
