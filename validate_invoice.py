# SemEng 100-character assignment ID proof (c)
def validate_invoice(amount: float) -> bool:
    if amount <= 0:
        raise ValueError("Invoice amount must be positive")
    return True
