import subprocess
import sys
import os

try:
    from PIL import Image, ImageTk
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow"])
    from PIL import Image, ImageTk

import tkinter as tk


script_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(script_dir, "monika.png")

root = tk.Tk()
root.title("Just Monika.")
root.configure(bg="#000000")  


root.attributes("-fullscreen", True)


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

try:
   
    img = Image.open(image_path)
    
    
    img_ratio = img.width / img.height
    new_height = screen_height - 100
    new_width = int(new_height * img_ratio)
    
    img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
    tk_img = ImageTk.PhotoImage(img)

   
    monika_label = tk.Label(root, image=tk_img, bg="#000000")
    monika_label.pack(expand=True, pady=10)

except FileNotFoundError:
    error_label = tk.Label(root, text="Błąd! Nie znaleziono monika.png", fg="red", bg="#000000", font=("Arial", 16))
    error_label.pack(expand=True)


text_label = tk.Label(root, text="Just Monika.", font=("Courier", 24, "bold"), bg="#000000", fg="#ffffff")
text_label.pack(pady=20)


# ==========================================
# 🔒 BLOKADA ZAMYKANIA OKNA (JUST MONIKA)
# ==========================================

# Ta pusta funkcja sprawia, że próba zamknięcia okna nic nie robi
def zablokuj_zamkniecie():
    pass

# Przechwytujemy Alt + F4 oraz systemowy przycisk X
root.protocol("WM_DELETE_WINDOW", zablokuj_zamkniecie)

# Blokujemy klawisz Escape (teraz nic nie zrobi)
root.bind("<Escape>", lambda event: "break")

# Opcjonalnie: Blokujemy też Alt+F4 jako skrót klawiszowy w Tkinterze
root.bind("<Alt-F4>", lambda event: "break")
# ==========================================


# Uruchomienie okna
root.mainloop()
