import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Sign Up")
root.geometry("400x600")

orange_color = "#FFA500"
dark_color = "#282828"
green_color = "#008000"
red_color = "#FF0000"

root.configure(bg=dark_color)
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", background=dark_color, foreground="white")
style.configure("TLabel", background=dark_color, foreground="white")
style.configure("TEntry", background="white", foreground="black")
style.configure("TCombobox", background="white", foreground="black")

header_frame = tk.Frame(root, bg=orange_color, height=50)
header_frame.pack(fill=tk.X)

header_label = tk.Label(header_frame, text="Sign Up", font=("Arial", 16, "bold"), bg=orange_color, fg="white")
header_label.pack(pady=10)

input_frame = tk.Frame(root, bg=dark_color)
input_frame.pack(pady=20, padx=20)

labels = ["First Name", "Last Name", "Screen Name", "Date of Birth (MM/DD/YYYY)", "Gender", "Country", "E-mail", "Phone", "Password", "Confirm Password"]
entries = []

for label_text in labels:
    label = ttk.Label(input_frame, text=label_text)
    label.grid(row=labels.index(label_text), column=0, sticky=tk.W, pady=5)

    if label_text == "Date of Birth (MM/DD/YYYY)":
        month_var = tk.StringVar()
        day_var = tk.StringVar()
        year_var = tk.StringVar()

        month_combo = ttk.Combobox(input_frame, textvariable=month_var, values=list(range(1, 13)))
        day_combo = ttk.Combobox(input_frame, textvariable=day_var, values=list(range(1, 32)))
        year_combo = ttk.Combobox(input_frame, textvariable=year_var, values=list(range(1900, 2024))) # Примерный диапазон

        month_combo.grid(row=labels.index(label_text), column=1, sticky=tk.W, pady=5)
        day_combo.grid(row=labels.index(label_text), column=2, sticky=tk.W, pady=5)
        year_combo.grid(row=labels.index(label_text), column=3, sticky=tk.W, pady=5)
    elif label_text == "Gender":
        gender_var = tk.StringVar(value="Male")
        male_radio = ttk.Radiobutton(input_frame, text="Male", variable=gender_var, value="Male")
        female_radio = ttk.Radiobutton(input_frame, text="Female", variable=gender_var, value="Female")
        male_radio.grid(row=labels.index(label_text), column=1, sticky=tk.W, pady=5)
        female_radio.grid(row=labels.index(label_text), column=2, sticky=tk.W, pady=5)
    elif label_text == "Country":
         country_combo = ttk.Combobox(input_frame, values=["USA", "Canada", "Russia", "Other"]) # Пример списка стран
         country_combo.grid(row=labels.index(label_text), column=1, sticky=tk.W, pady=5)
    else:
        entry = ttk.Entry(input_frame)
        entry.grid(row=labels.index(label_text), column=1, sticky=tk.W, pady=5)
        entries.append(entry)


terms_var = tk.BooleanVar()
terms_check = ttk.Checkbutton(input_frame, text="I agree to the Terms of Use", variable=terms_var)
terms_check.grid(row=len(labels), columnspan=2, sticky=tk.W, pady=10)

submit_button = tk.Button(input_frame, text="Submit", bg=green_color, fg="white", command=lambda: print("Submitted!")) # Замените на нужную функцию
submit_button.grid(row=len(labels) + 1, column=0, pady=10)


cancel_button = tk.Button(input_frame, text="Cancel", bg=red_color, fg="white", command=root.destroy)
cancel_button.grid(row=len(labels) + 1, column=1, pady=10)


root.mainloop()