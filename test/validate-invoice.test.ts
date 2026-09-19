import { validateInvoice } from "../src/validate-invoice.ts";

export function test_validateInvoiceRejectsZero(): void {
  try {
    validateInvoice({ amount: 0 });
    throw new Error("Expected validation to reject the invoice");
  } catch (error) {
    if (!(error instanceof Error) || error.message !== "Invoice amount must be positive") {
      throw error;
    }
  }
}

test_validateInvoiceRejectsZero();