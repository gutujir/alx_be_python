class BankAccount:
    def __init__(self, initial_balance: float = 0.0):
        # Encapsulated balance (conventionally "private" by prefixing with underscore)
        self._account_balance = float(initial_balance)

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self._account_balance += amount

    def withdraw(self, amount: float) -> bool:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self._account_balance:
            return False
        self._account_balance -= amount
        return True

    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:,.2f}")

    def get_balance(self) -> float:
        # Accessor if needed programmatically
        return self._account_balance

    def __str__(self):
        return f"BankAccount(balance=${self._account_balance:,.2f})"
