import pandas as pd
import matplotlib.pyplot as plt

# Załadowanie danych
df = pd.DataFrame({'A': [1, 2, 3, 4], 'B': [4, 5, 6, 7]})

# Proste statystyki opisowe
print(df.describe())

# Tworzenie wykresu skrzynkowego
df.plot.box()
plt.show()
