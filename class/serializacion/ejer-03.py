import json

mensaje = {"emisor": "felipe", "contenido": "Hola, clase", "etiquetas": ("a", "b")}

texto = json.dumps(mensaje, ensure_ascii=False)
print(texto)

copia = json.loads(texto)
print(f"Los mensajes son iguales: {copia == mensaje}")
