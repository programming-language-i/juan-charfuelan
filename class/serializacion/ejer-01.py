import pickle

mensaje = {"emisor": "ana", "contenido": "hola", "etiquetas": ("a", "b")}

datos = pickle.dumps(mensaje)  # objeto → bytes
print(datos[:30], len(datos))

copia = pickle.loads(datos)  # bytes → objeto
print(copia == mensaje, copia is mensaje)  # True False: una copia, no el mismo objeto

print(f"\n{datos}")
print(f"\n{copia}")
