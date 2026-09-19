from validate_invoice import validate_invoice


def test_validate_invoice_rejects_zero() -> None:
    try:
        validate_invoice(0)
        raise AssertionError("Expected validation to reject the invoice")
    except ValueError as error:
        assert str(error) == "Invoice amount must be positive"
