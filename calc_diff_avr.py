import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt

# Подключение к БД и выполнение запроса
engine = create_engine('your_database_connection_string')
query = """
SELECT 
    u.gender,
    AVG(o.order_cost) as avg_order_cost,
    COUNT(o.order_id) as order_count
FROM поездки o
JOIN пользователи u ON o.user_id = u.user_id
WHERE o.order_dt BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY u.gender;
"""

df = pd.read_sql(query, engine)

# Расчет разницы среднего чека
avg_male = df[df['gender'] == 'М']['avg_order_cost'].values[0]
avg_female = df[df['gender'] == 'Ж']['avg_order_cost'].values[0]
difference = avg_male - avg_female

print(f"Средний чек мужчин: {avg_male:.2f}")
print(f"Средний чек женщин: {avg_female:.2f}")
print(f"Разница: {difference:.2f}")
