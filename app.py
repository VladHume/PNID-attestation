def add(a: int, b: int) -> int:
    return a + b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero")

    return a / b


if __name__ == "__main__":
    print("Application is running")
