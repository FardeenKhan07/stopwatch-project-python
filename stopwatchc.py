import tkinter as tk
from tkinter import Label, Button
import time

class Stopwatch:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch")
        self.running = False
        self.start_time = None
        self.elapsed_time = 0

        self.label = Label(root, text="00:00:00", font=("Arial", 40))
        self.label.pack()

        self.start_button = Button(root, text="Start", command=self.start, font=("Arial", 15))
        self.start_button.pack()

        self.stop_button = Button(root, text="Stop", command=self.stop, font=("Arial", 15))
        self.stop_button.pack()

        self.reset_button = Button(root, text="Reset", command=self.reset, font=("Arial", 15))
        self.reset_button.pack()

    def update_timer(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
            self.label.config(text=self.format_time(self.elapsed_time))
            self.root.after(100, self.update_timer)

    def format_time(self, seconds):
        mins, secs = divmod(int(seconds), 60)
        hours, mins = divmod(mins, 60)
        return f"{hours:02}:{mins:02}:{secs:02}"

    def start(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time
            self.update_timer()

    def stop(self):
        if self.running:
            self.running = False

    def reset(self):
        self.running = False
        self.elapsed_time = 0
        self.label.config(text="00:00:00")

root = tk.Tk()
stopwatch = Stopwatch(root)
root.mainloop()