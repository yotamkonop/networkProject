import tkinter as tk

def save_and_quit():
    text = text_box.get("1.0", tk.END).strip()
    with open("description.txt", "w", encoding="utf-8") as f:
        f.write(text)
    root.destroy()

# Set up GUI window
root = tk.Tk()
root.title("Enter Description")

# Create and pack the widgets
tk.Label(root, text="Enter your description:").pack(pady=(10, 0))

text_box = tk.Text(root, height=10, width=50)
text_box.pack(padx=10, pady=10)

enter_button = tk.Button(root, text="Enter", command=save_and_quit)
enter_button.pack(pady=(0, 10))

# Start the GUI loop
root.mainloop()