class Mayor:
    def __init__(self) -> None:
        pass

    def mayor(self, numero1: int, numero2: int) -> int | None:
        result = 0
        if numero1 > numero2:
            result = numero1
        elif numero2 > numero1:
            result = numero2
        else:
            result = None
        return result
