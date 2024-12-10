import tkinter as tk
import os, sys, time, random as rnd
import threading

def generate_random(label, lower, upper, refresh_time):
    while True:
        random_number = rnd.randint(lower, upper)
        label.config(text=f"{random_number}\n[{lower}, {upper}]\nrefresh interval = {refresh_time}s")
        time.sleep(refresh_time)
    return

def setup_dashboard():
    app = tk.Tk()
    app.title("Random Number Dashboard with Multithreading")

    configurations = [
        (1, 50, 20, "aquamarine"),
        (-20, 20, 17, "coral"),
        (-200, -50, 6, "khaki"),
        (10, 30, 28, "skyblue"),
        (-70, 70, 10, "plum"),
        (50, 300, 9, "lightgreen")
    ]
    labels = []
    for idx, (lower_bound, upper_bound, refresh_time, bg_color) in enumerate(configurations):
        label_widget = tk.Label(app, text="0", font=("Arial", 14), width=18, height=6, bg=bg_color)
        label_widget.grid(row=idx // 2, column=idx % 2, padx=15, pady=15)
        labels.append((label_widget, lower_bound, upper_bound, refresh_time))

    for label, lower_bound, upper_bound, refresh_time in labels:
        thread = threading.Thread(target=generate_random, args=(label, lower_bound, upper_bound, refresh_time))
        thread.daemon = True
        thread.start()

    app.mainloop()

if __name__ == "__main__":
    setup_dashboard()
