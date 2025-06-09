import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

conn = sqlite3.connect('db/lesson.db')

# sql query to get the order_id and total_price, join
query = """
SELECT o.order_id AS order_id, SUM(li.quantity * p.price) AS total_price
FROM orders o
JOIN line_items li ON o.order.id = li.order_id
JOIN products p ON li.product_id = p.id
GROUP BY o.order_id
ORDER BY o.order_id;
"""

# loading the dataframe
df = pd.read_sql_query(query, conn)
conn.close()

# order_id is the dataframe var
order_id = df.total_price

# find the cumulative function


def cumulative(row):
    totals_above = df['total_price'][0:row.name+1]
    return totals_above.sum()


# using apply()
df['cumulative'] = df.apply(cumulative, axis=1)

# plotting the cumulative revenue vs the order_id
plt.figure(figsize=(10, 6))
plt.plot(df['order_id'], df['cumulative'],
         marker='o', label='Cumulative Revenue')
plt.xlabel('Order ID')
plt.ylabel('Cumulative Revenue ($)')
plt.title('Cumulative Revenue vs. Order ID')
plt.grid(True)
plt.legend()
plt.tight_layout()

# show the plot
plt.show()
