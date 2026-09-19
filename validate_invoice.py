# SemEng staging candidate p0-staging-py-003
def validate_invoice(amount: float) -> bool:
    if amount <= 0:
        raise ValueError("Invoice amount must be positive")
    return True
