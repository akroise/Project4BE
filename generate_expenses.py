import pandas as pd
import random
from datetime import datetime, timedelta

# --- Configuration ---
NUM_ROWS = 10000
USER_IDS = list(range(1, 11))  # Simulate 10 users (1–10)
EXPENSE_TYPES = [
    "Cafeteria",
    "Uber/Rapido",
    "Flat",
    "Self",
    "Others"
]
COMMENTS = [
    "Paid for lunch",
    "Monthly rent transfer",
    "Grocery shopping",
    "Recharge and utilities",
    "Weekend movie",
    "Cab to office",
    "Snacks with friends",
    "Online subscription renewal",
    "Flat maintenance charges",
    "Fuel refill",
    "Gift purchase"
]

# --- Helper Functions ---
def random_datetime(start, end):
    """Generate random datetime between two datetime objects."""
    delta = end - start
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return start + timedelta(seconds=random_seconds)

# --- Generate Data ---
start_date = datetime(2025, 1, 1)
end_date = datetime.now()

data = []

for _ in range(NUM_ROWS):
    user_id = random.choice(USER_IDS)
    expense_type = random.choice(EXPENSE_TYPES)
    date_time = random_datetime(start_date, end_date)
    updated = date_time + timedelta(days=random.randint(0, 5))  # occasionally updated later
    amount = round(random.uniform(50, 5000), 2)
    additional_comments = random.choice(COMMENTS)
    
    row = {
        "id": random.randint(100000, 999999),
        "user_id": user_id,
        "date_time": date_time.strftime("%Y-%m-%d %H:%M:%S"),
        "expense_type": expense_type,
        "additional_comments": additional_comments,
        "is_active": True,
        "updated": updated.strftime("%Y-%m-%d %H:%M:%S"),
        "amount": amount
    }
    data.append(row)

# --- Create DataFrame ---
df = pd.DataFrame(data)

# --- Save to CSV ---
df.to_csv("expenses_data_multiuser.csv", index=False)

print(f"✅ Successfully generated {NUM_ROWS} expense records for {len(USER_IDS)} users.")
print("📁 File saved as 'expenses_data_multiuser.csv'")
