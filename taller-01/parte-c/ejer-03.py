from concurrent.futures import ProcessPoolExecutor


def cuadrado(n):
    return n * n


if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=2) as pool:
        print(list(pool.map(cuadrado, range(4))))
