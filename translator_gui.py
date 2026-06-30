import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator

# Language codes
languages = {
    "English": "en",
    "Telugu": "te",
    "Hindi": "hi",
    "Tamil": "ta",
    "Kannada": "kn",
    "Malayalam": "ml",
    "French": "fr",
    "German": "de"
}

def translate_text():
    text = input_text.get("1.0", tk.END).strip()

    if not text:
        return

    source_lang = languages[source_combo.get()]
    target_lang = languages[target_combo.get()]

    translated = GoogleTranslator(
        source=source_lang,
        target=target_lang
    ).translate(text)

    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, translated)
def copy_text():
    translated = output_text.get("1.0", tk.END)

    root.clipboard_clear()
    root.clipboard_append(translated)

def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

# Main window
root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("700x600")

title = tk.Label(
    root,
    text="Language Translation Tool",
    font=("Arial", 16, "bold")
)
title.pack(pady=10)

# Source language
tk.Label(root, text="Source Language").pack()

source_combo = ttk.Combobox(
    root,
    values=list(languages.keys())
)
source_combo.pack()
source_combo.set("English")

# Target language
tk.Label(root, text="Target Language").pack()

target_combo = ttk.Combobox(
    root,
    values=list(languages.keys())
)
target_combo.pack()
target_combo.set("Telugu")

# Input text
tk.Label(root, text="Enter Text").pack()

input_text = tk.Text(root, height=8, width=70)
input_text.pack(pady=10)

# Translate button
translate_button = tk.Button(
    root,
    text="Translate",
    command=translate_text
)
translate_button.pack(pady=10)
copy_button = tk.Button(
    root,
    text="Copy",
    command=copy_text
)
copy_button.pack(pady=5)

clear_button = tk.Button(
    root,
    text="Clear",
    command=clear_text
)
clear_button.pack(pady=5)

# Output text
tk.Label(root, text="Translated Text").pack()

output_text = tk.Text(root, height=8, width=70)
output_text.pack(pady=10)

root.mainloop()