import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

conn = sqlite3.connect('db/lesson.db')


query = """
SELECT last_name, SUM(price * quantity) AS revenue FROM employees e JOIN orders o ON e.employee_id = o.employee_id JOIN line_items l ON o.order_id = l.order_id JOIN products p ON l.product_id = p.product_id GROUP BY e.employee_id;
"""

# loading the dataframe
employee_results = pd.read_sql_query(query, conn)
conn.close()

# plot
employee_results.set_index('last_name')['revenue'].plot(
    kind='bar', color='skyblue', figsize=(10, 6))
plt.title('Employee Revenue by Last Name')
plt.xlabel('Last Name')
plt.ylabel('Revenue')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
