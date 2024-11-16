# -*- coding: utf-8 -*-
"""lab02.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Z0ps9lzH6jpyZ2U2IKsgefYnr8xTC9RQ
"""

import matplotlib.pyplot as plt
import numpy as np

class TradingAgent:
    def __init__(self, average_price, critical_stock=15, min_order=8, regular_order=20,
                 monthly_budget=4000, max_stock_capacity=80, max_monthly_orders=150, restock_frequency=2):
        self.average_price = average_price
        self.critical_stock = critical_stock
        self.min_order = min_order
        self.regular_order = regular_order
        self.monthly_budget = monthly_budget
        self.current_budget = monthly_budget
        self.max_stock_capacity = max_stock_capacity
        self.max_monthly_orders = max_monthly_orders
        self.total_ordered = 0
        self.stock_level = max_stock_capacity // 2
        self.last_order_day = -restock_frequency

        # Constraints
        self.restock_frequency = restock_frequency  # Minimum days between orders

        # Data for plotting
        self.days = []
        self.stock_levels = []
        self.budgets = []
        self.orders_placed = []

    def check_price_discount(self, current_price):
        """Checks if the current price is at least 20% lower than the average price."""
        discount_threshold = 0.8 * self.average_price
        return current_price < discount_threshold

    def should_order_more(self, current_price, day):
        """
        Determines whether to place an order based on price, stock, and constraints.
        If stock is critically low, considers an emergency purchase.
        """
        if day - self.last_order_day < self.restock_frequency:
            return 0  # Skip ordering if it hasn't been long enough since the last order

        # Emergency purchase mode for critically low stock
        if self.stock_level < self.critical_stock:
            return self.min_order

        # Regular order if price is discounted and stock allows
        elif self.check_price_discount(current_price) and self.stock_level + self.regular_order <= self.max_stock_capacity:
            return self.regular_order

        return 0

    def place_order(self, current_price, day):
        """Places an order based on conditions and updates budget, stock, and order data."""
        tobuy = self.should_order_more(current_price, day)

        # Apply bulk discount if ordering more than 20 units
        discount_rate = 0.95 if tobuy > 20 else 1
        total_cost = tobuy * current_price * discount_rate

        # Constraints: Check budget and monthly limits
        if (self.total_ordered + tobuy > self.max_monthly_orders) or (total_cost > self.current_budget):
            tobuy = 0

        if tobuy > 0:
            self.current_budget -= total_cost
            self.stock_level += tobuy
            self.total_ordered += tobuy
            self.last_order_day = day  # Update last order day
            print(f"Day {day}: Ordered {tobuy} units. Total cost: {total_cost} BDT. Stock level: {self.stock_level}.")
        else:
            print(f"Day {day}: No order placed. Stock level: {self.stock_level}.")

        # Logging data for plotting
        self.days.append(day)
        self.stock_levels.append(self.stock_level)
        self.budgets.append(self.current_budget)
        self.orders_placed.append(tobuy)

    def reset_month(self):
        """Resets budget and total ordered for the new month."""
        self.current_budget = self.monthly_budget
        self.total_ordered = 0
        self.last_order_day = -self.restock_frequency

# Initialize the TradingAgent with new constraints
agent = TradingAgent(average_price=700)

# Run a 30-day simulation with fluctuating prices
np.random.seed(0)
price_trend = 700 + 50 * np.sin(np.linspace(0, 3 * np.pi, 30))

for day in range(1, 31):
    current_price = price_trend[day - 1]
    agent.place_order(current_price, day)

    # Reset at the end of the month for simplicity (e.g., day 30)
    if day == 30:
        agent.reset_month()

# Plotting the results
plt.figure(figsize=(15, 8))

# Plot stock level over time
plt.subplot(3, 1, 1)
plt.plot(agent.days, agent.stock_levels, color='blue', label="Stock Level")
plt.axhline(y=agent.critical_stock, color='red', linestyle='--', label="Critical Stock Level")
plt.axhline(y=agent.max_stock_capacity, color='green', linestyle='--', label="Max Stock Capacity")
plt.xlabel("Day")
plt.ylabel("Stock Level")
plt.title("Stock Level Over Time")
plt.legend()

# Plot remaining budget over time
plt.subplot(3, 1, 2)
plt.plot(agent.days, agent.budgets, color='purple', label="Remaining Budget")
plt.axhline(y=0, color='red', linestyle='--', label="Budget Exhausted")
plt.xlabel("Day")
plt.ylabel("Remaining Budget (BDT)")
plt.title("Remaining Budget Over Time")
plt.legend()

# Plot orders placed each day
plt.subplot(3, 1, 3)
plt.bar(agent.days, agent.orders_placed, color='orange', label="Units Ordered")
plt.xlabel("Day")
plt.ylabel("Units Ordered")
plt.title("Units Ordered Per Day")
plt.legend()

plt.tight_layout()
plt.show()