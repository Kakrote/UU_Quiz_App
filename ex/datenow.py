import customtkinter as ctk
import time

app = ctk.CTk()

start = time.time()

def updateTimer():
    global timerLabel
    t = time.time() - start
    t = int(t)
    print(t)
    timerLabel.configure(text=str(t))
    app.after(500, updateTimer)

    pass

timerLabel = ctk.CTkLabel(app, text="")
timerLabel.pack()

app.after(500, updateTimer)

app.mainloop()