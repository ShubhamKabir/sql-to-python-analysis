import pandas as pd

data = {
    "order_id": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "customer": ["Alex", "Beth", "Alex", "Drew", "Beth", "Drew", "Chris", "Chris", "Alex", "Drew"],
    "product": ["Laptop", "Mouse", "Laptop", "Monitor", "Mouse", "Monitor", "Laptop", "Mouse", "Monitor", "Laptop"],
    "amount": [1200, 25, 1200, 300, 25, 300, 1200, 25, 300, 1200],
    "city": ["NYC", "London", "NYC", "Tokyo", "London", "Tokyo", "London", "NYC", "Tokyo", "NYC"],
    "date": ["2026-01-01", "2026-01-02", "2026-01-03", "2026-01-04", "2026-01-05", 
             "2026-01-06", "2026-01-07", "2026-01-08", "2026-01-09", "2026-01-10"]
}

pd.DataFrame(data).to_csv("sales.csv", index=False)
print("Project database (sales.csv) initialized.")