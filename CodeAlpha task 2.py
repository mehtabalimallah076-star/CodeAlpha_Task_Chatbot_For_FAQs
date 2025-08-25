import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator
import pyttsx3
import pyperclip

# Initialize TTS engine
engine = pyttsx3.init()

# Function to translate
def translate_text():
    try:
        src_lang = source_lang.get()
        dest_lang = target_lang.get()
        text = input_text.get("1.0", tk.END).strip()

        if text == "":
            messagebox.showwarning("Warning", "Please enter some text to translate!")
            return

        translated = GoogleTranslator(source=src_lang, target=dest_lang).translate(text)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated)
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {e}")

# Function to copy translated text
def copy_text():
    translated = output_text.get("1.0", tk.END).strip()
    if translated:
        pyperclip.copy(translated)
        messagebox.showinfo("Copied", "Translated text copied to clipboard!")

# Function for Text-to-Speech
def speak_text():
    translated = output_text.get("1.0", tk.END).strip()
    if translated:
        engine.say(translated)
        engine.runAndWait()
    else:
        messagebox.showwarning("Warning", "No translated text to speak!")

# GUI Window
root = tk.Tk()
root.title("Language Translation Tool")
root.geometry("650x500")
root.config(bg="#f2f2f2")

# Labels
tk.Label(root, text="Enter Text:", font=("Arial", 12), bg="#f2f2f2").pack(pady=5)
input_text = tk.Text(root, height=5, width=70)
input_text.pack(pady=5)

# Dropdowns for language selection
frame = tk.Frame(root, bg="#f2f2f2")
frame.pack(pady=10)

tk.Label(frame, text="From:", font=("Arial", 10), bg="#f2f2f2").grid(row=0, column=0, padx=5)
source_lang = ttk.Combobox(frame, values=["auto","en","ur","fr","de","es","ar","hi"], width=15)
source_lang.set("auto")  # default auto-detect
source_lang.grid(row=0, column=1, padx=5)

tk.Label(frame, text="To:", font=("Arial", 10), bg="#f2f2f2").grid(row=0, column=2, padx=5)
target_lang = ttk.Combobox(frame, values=["en","ur","fr","de","es","ar","hi"], width=15)
target_lang.set("ur")  # default Urdu
target_lang.grid(row=0, column=3, padx=5)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#f2f2f2")
btn_frame.pack(pady=10)

translate_btn = tk.Button(btn_frame, text="Translate", command=translate_text, font=("Arial", 12), bg="#4CAF50", fg="white")
translate_btn.grid(row=0, column=0, padx=10)

copy_btn = tk.Button(btn_frame, text="Copy", command=copy_text, font=("Arial", 12), bg="#2196F3", fg="white")
copy_btn.grid(row=0, column=1, padx=10)

speak_btn = tk.Button(btn_frame, text="Speak", command=speak_text, font=("Arial", 12), bg="#FF5722", fg="white")
speak_btn.grid(row=0, column=2, padx=10)

# Output box
tk.Label(root, text="Translated Text:", font=("Arial", 12), bg="#f2f2f2").pack(pady=5)
output_text = tk.Text(root, height=5, width=70)
output_text.pack(pady=5)

# Run GUI
root.mainloop()
