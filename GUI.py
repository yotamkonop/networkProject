import tkinter as tk

def run_gui(msg_queue=None, on_send=None):
    def check_queue():
        if msg_queue:
            while not msg_queue.empty():
                msg = msg_queue.get()
                chat_box.insert(tk.END, msg + "\n")
        root.after(100, check_queue)

    def send_message():
        msg = entry.get()
        if msg.strip() == "":
            return
        chat_box.insert(tk.END, f"You: {msg}\n")  # Add to message area
        entry.delete(0, tk.END)                   # Clear input
        if on_send:
            on_send(msg)  # Call external function to send over socket

    # --- GUI setup ---
    root = tk.Tk()
    root.title("Chat")

    # Chat history box (top section)
    chat_box = tk.Text(root, height=20, width=50)
    chat_box.pack(padx=10, pady=5)

    # Bottom section: entry + send button
    bottom_frame = tk.Frame(root)
    entry = tk.Entry(bottom_frame, width=40)
    entry.pack(side=tk.LEFT, padx=5)
    send_btn = tk.Button(bottom_frame, text="Send", command=send_message)
    send_btn.pack(side=tk.LEFT)
    bottom_frame.pack(pady=5)

    check_queue()  # Start polling for messages
    root.mainloop()
