class BalloonTooFull(Exception):
    pass


class Balloon:
    def __init__(self) -> None:
        self.capacity = 0
        self.amount = 0

    def pump(self) -> None:
        self.amount += 3
        if self.amount > self.capacity:
            raise BalloonTooFull("Pop!")

    def release(self) -> None:
        self.amount -= 2
        self.amount = max(0, self.amount)


class SwordBalloon(Balloon):
    def __init__(self) -> None:
        super().__init__()
        self.capacity = 5


class DogBalloon(Balloon):
    def __init__(self) -> None:
        super().__init__()
        self.capacity = 7


class TriforceBalloon(Balloon):
    def __init__(self) -> None:
        super().__init__()
        self.capacity = 11
