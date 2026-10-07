# Customer Lifetime Value (CLV) Calculator

A Python script that calculates Customer Lifetime Value for a group of customers and identifies which ones are high-value, using NumPy for fast array-based calculations.

## How it works
- CLV is calculated as: average order value × purchase frequency × customer lifespan (years)
- All customers' CLV are calculated in a single vectorized operation (no loop needed)
- Customers with a CLV at or above a threshold ($2,000) are flagged as high-value
- Reports the average CLV across all customers

## How to run
```bash
python clv_calculator.py
```

## What I learned
- Using NumPy array multiplication to calculate a value for every customer at once, instead of looping through each one individually
- Using boolean array indexing (`customer_ids[is_high_value]`) to filter one array based on a condition from another array
- Using `np.mean()` for quick aggregate statistics across the dataset

## Dependencies
Requires NumPy:
```bash
pip install numpy
```
