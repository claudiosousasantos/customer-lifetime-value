import numpy as np

# Step 1: Sample customer data
customer_ids = np.array(["C001", "C002", "C003", "C004", "C005"])
avg_order_value = np.array([50, 120, 35, 200, 80])
purchase_frequency = np.array([12, 4, 24, 2, 6])
customer_lifespan = np.array([3, 5, 1, 8, 2])

# Step 2: Calculate CLV for everyone at once
clv = avg_order_value * purchase_frequency * customer_lifespan

# Step 3: Print each customer's CLV
for i in range(len(customer_ids)):
    print(f"{customer_ids[i]}: CLV = ${clv[i]:.2f}")

# Step 4: Flag high-value customers
high_value_threshold = 2000
is_high_value = clv >= high_value_threshold
high_value_customers = customer_ids[is_high_value]
print("\n💎 High-value customers:", high_value_customers)

# Step 5: Average CLV
average_clv = np.mean(clv)
print(f"\nAverage CLV across all customers: ${average_clv:.2f}")