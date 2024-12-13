import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Dane
technologies = ['Spark', 'Pandas', 'Python', 'PHP']
fee = [25000, 20000, 15000, 18000]
duration = ['50 Days', '35 Days', np.nan, '15 Days']
discount = [2000, 1000, 800, 500]

# Utworzenie DataFrame
data = {
    'Courses': technologies,
    'Fee': fee,
    'Duration': duration,
    'Discount': discount
}
df = pd.DataFrame(data)

# Wyświetlenie DataFrame
print(df)

# Rysowanie wykresu z rabatami
plt.figure(figsize=(10, 6))
bar_width = 0.35
index = np.arange(len(df['Courses']))

# Słupki dla opłat
plt.bar(index, df['Fee'], bar_width, label='Fee', color='blue')

# Słupki dla rabatów
plt.bar(index + bar_width, df['Discount'], bar_width, label='Discount', color='red')

# Dodanie tytułu i etykiet osi
plt.title('Course Fees and Discounts')
plt.xlabel('Courses')
plt.ylabel('Amount')
plt.xticks(index + bar_width / 2, df['Courses'])

# Dodanie legendy
plt.legend()

# Wyświetlenie wykresu
plt.show()
