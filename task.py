transactions = [
  {"reference": "TX001", "amount": 1200, "status": "success"},
  {"reference": "TX002", "amount": 500, "status": "failed"},
  {"reference": "TX003", "amount": 3000, "status": "success"},
  {"reference": "TX004", "amount": 800, "status": "pending"}
]
total_successful_amount = sum(txn["amount"] for txn in transactions if txn["status"] == "success")
print(f"Total amount of successful transactions: {total_successful_amount}")

count_successful_transactions = sum(1 for txn in transactions if txn["status"] == "success")
print(f"Number of successful transactions: {count_successful_transactions}")

def failures(transactions):
    failed_transactions = [txn for txn in transactions if txn["status"] == "failed"]
    return failed_transactions

failed_transactions = failures(transactions)
print(f"Failed transactions: {failed_transactions}")

highest_transaction = max(transactions, key=lambda txn: txn["amount"])
print(f"Transaction with the highest amount: {highest_transaction}")

def amount_above_1000(transactions):
    return [txn for txn in transactions if txn["amount"] > 1000]

transactions_above_1000 = amount_above_1000(transactions)
print(f"Transactions with amount above 1000: {transactions_above_1000}")

grouped_transactions = {}
for txn in transactions:
    status = txn["status"]
    if status not in grouped_transactions:
        grouped_transactions[status] = []
    grouped_transactions[status].append(txn)

print(f"Grouped transactions: {grouped_transactions}")