import tkinter as tk
from tkinter import filedialog

def wybierz_plik():
    # Otwórz okno dialogowe do wyboru pliku
    plik = filedialog.askopenfilename(title="Wybierz plik")
    if plik:
        print(f"Wybrano plik: {plik}")

# Tworzenie okna aplikacji
root = tk.Tk()
root.withdraw()  # Ukryj główne okno

# Wywołanie eksploratora
wybierz_plik()