class Glass:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.amount = 0

    def pour_in(self, amount) -> None:
        if amount < 0:
            raise ValueError("Amount to pour in must be positive.")
        self.amount = min(self.amount + amount, self.capacity)

    def pour_out(self, amount) -> None:
        if amount < 0:
            raise ValueError("Amount to pour out must be positive.")
        self.amount = max(self.amount - amount, 0)
