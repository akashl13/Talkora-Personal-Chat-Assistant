# Talkora.py
from customtkinter import *
from ChatBox import get_response
import time
import threading

# Main window setup
root = CTk()
root.title("Talkora - Personal Chat Assistant")
root.geometry("600x750")
root.configure(fg_color="#F2F2F2")

# Fonts
FONT_HEADER = ("Arial Rounded MT Bold", 24)
FONT_MSG = ("Segoe UI", 14)

# Function to create message bubbles
def message_bubble(text, sender):
    fg = "#cce5ff" if sender == "user" else "#e8e8e8"
    anchor = "e" if sender == "user" else "w"
    bubble = CTkFrame(message_frame, fg_color=fg, corner_radius=15)
    txt = CTkLabel(bubble, text=text, text_color="black", font=FONT_MSG,
                   wraplength=450, justify="left")
    txt.pack(padx=12, pady=6)
    bubble.pack(anchor=anchor, padx=20, pady=5)
    root.after(100, lambda: message_frame._parent_canvas.yview_moveto(1.0))

# Send user message and handle bot reply
def send_message():
    user_text = com.get().strip()
    if user_text == "":
        return
    message_bubble(f"You: {user_text}", "user")
    com.delete(0, END)
    typing_label = CTkLabel(message_frame, text="Talkora is typing", text_color="gray")
    typing_label.pack(anchor="w", padx=20, pady=5)
    message_frame._parent_canvas.yview_moveto(1.0)

    def get_bot_reply():
        for i in range(3):
            typing_label.configure(text=f"Talkora is typing{'.' * (i % 4)}")
            time.sleep(0.15)
        bot_reply = get_response(user_text)
        typing_label.destroy()
        message_bubble(f"Talkora: {bot_reply}", "bot")

    threading.Thread(target=get_bot_reply, daemon=True).start()

# Header frame
frame = CTkFrame(root, fg_color="#3D5AFE", corner_radius=0)
frame.pack(side="top", fill="x")

Talkora = CTkLabel(frame, text="Talkora - Your Personal Assistant",
                   text_color="white", font=FONT_HEADER)
Talkora.pack(padx=30, pady=20)

# Main frame
main_frame = CTkFrame(root, fg_color="#F2F2F2", corner_radius=0)
main_frame.pack(fill="both", expand=True)

# Scrollable chat area
message_frame = CTkScrollableFrame(main_frame, fg_color="white", corner_radius=15)
message_frame.pack(side="top", padx=30, pady=20, fill="both", expand=True)

# Input frame
input_frame = CTkFrame(root, fg_color="#1E1E1E", border_width=0, corner_radius=15)
input_frame.pack(side="bottom", fill="x", padx=20, pady=15)

# Text entry
com = CTkEntry(input_frame, fg_color="#2D2D2D", text_color="white",
               placeholder_text="Type your message...", placeholder_text_color="gray")
com.pack(side="left", fill="x", padx=20, pady=15, expand=True)
com.bind("<Return>", lambda event: send_message())

# Send button
submit_button = CTkButton(input_frame, fg_color="#3D5AFE", hover_color="#304FFE",
                          text="↵", width=40, command=send_message)
submit_button.pack(side="right", padx=15, pady=10)

# Welcome message
welcome = "Hi! I'm Talkora, your assistant.\nAsk me any question:\n"
message_bubble(welcome, "bot")

root.mainloop()
