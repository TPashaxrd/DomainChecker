import tkinter as tk
from tkinter import messagebox
import socket

# Domain kontrol fonksiyonu
def domain_checker():
    domain_name = domain_entry.get()
    if not domain_name:
        messagebox.showerror("Hata", "Enter a Domain addres")
        return
    
    try:
        # Alan adının DNS kaydını çözmeye çalış
        socket.gethostbyname(domain_name)
        result_label.config(text=f"{domain_name} Not Receivable.", fg="red")
    except socket.gaierror:
        result_label.config(text=f"{domain_name} Receivable", fg="green")

# GUI tasarımı
root = tk.Tk()
root.title("Domain Checker")
root.geometry("400x200")

# Başlık
title_label = tk.Label(root, text="Domain Checker", font=("Arial", 16))
title_label.pack(pady=10)

# Domain girişi
domain_entry = tk.Entry(root, width=30, font=("Arial", 12))
domain_entry.pack(pady=10)

# Kontrol butonu
check_button = tk.Button(root, text="Kontrol Et", command=domain_checker, font=("Arial", 12), bg="blue", fg="white")
check_button.pack(pady=10)

# Sonuç etiketi
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)

# Uygulama döngüsü
root.mainloop()


# Created by TPàshà
# https://github.com/TPashaxrd