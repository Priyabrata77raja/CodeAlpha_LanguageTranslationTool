import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator
LANGUAGES = {
    "English": "en",
    "Hindi": "hi",
    "Odia": "or",
    "Bengali": "bn",
    "Tamil": "ta",
    "Telugu": "te",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Kannada": "kn",
    "Malayalam": "ml",
    "Punjabi": "pa",
    "Urdu": "ur",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
}
def translate():
    text = entry.get().strip()
    if not text:
        output.config(text="Please enter some text.")
        return
    src_code = LANGUAGES.get(source_var.get(), "en")
    dest_code = LANGUAGES.get(target_var.get(), "hi")
    try:
        result = GoogleTranslator(source=src_code, target=dest_code).translate(text)
        output.config(text=result)
    except Exception as e:
        output.config(text=f"Error: {e}")
# Create Window
root = tk.Tk()
root.title("Language Translator")
root.geometry("400x350")
tk.Label(root, text="Enter Text").pack(pady=(10, 0))
entry = tk.Entry(root, width=40)
entry.pack(pady=5)
lang_names = list(LANGUAGES.keys())
tk.Label(root, text="Source Language").pack(pady=(10, 0))
source_var = tk.StringVar(value="English")
source_menu = ttk.Combobox(root, textvariable=source_var, values=lang_names, state="readonly", width=20)
source_menu.pack(pady=5)
tk.Label(root, text="Target Language").pack(pady=(10, 0))
target_var = tk.StringVar(value="Hindi")
target_menu = ttk.Combobox(root, textvariable=target_var, values=lang_names, state="readonly", width=20)
target_menu.pack(pady=5)
tk.Button(root, text="Translate", command=translate).pack(pady=15)
output = tk.Label(root, text="", font=("Arial", 12), wraplength=350, fg="blue")
output.pack(pady=5)
root.mainloop()
