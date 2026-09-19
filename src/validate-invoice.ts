export interface Invoice {
  amount: number;
}

export function validateInvoice(invoice: Invoice): true {
  if (invoice.amount <= 0) {
    throw new Error("Invoice amount must be positive");
  }
  return true;
}
