import customtkinter as ctk
from typing import Any


class MyFrame(ctk.CTk):
    def __init__(self, master: Any):
        super().__init__(master)

        self.new_frame = None  # Initialize a variable to store the new frame (if any)

        self.button = ctk.CTkButton(self, text="Open New Frame", command=self.open_new_frame)
        self.button.pack()

        self.button2 = ctk.CTkButton(self, text="Open Different Frame", command=self.open_new_frame2)
        self.button2.pack()

    def open_new_frame(self):
        # Check if a new frame already exists
        if self.new_frame is not None:
            self.new_frame.destroy()  # Destroy existing frame before creating a new one

        # Create and pack the new frame
        self.new_frame1 = ctk.CTkFrame(self)
        self.new_frame1.pack(padx=20, pady=20, fill="both", expand=True)

    def open_new_frame2(self):
        # Similar logic to open_new_frame, but with a different name for clarity
        if self.new_frame is not None:
            self.new_frame.destroy()
        self.new_frame = ctk.CTkFrame(self)
        self.new_frame.pack(padx=20, pady=20, fill="both", expand=True)

        self.new_frame = ctk.CTkFrame(self, bg="blue")  # Set a different background color for this frame
        self.new_frame.pack(padx=20, pady=20, fill="both", expand=True)


app = MyFrame(None)
app.mainloop()
