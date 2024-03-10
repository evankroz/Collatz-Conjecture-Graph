import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

def collatz_sequence(num):
    sequence_list = [num]
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        sequence_list.append(num)
    return sequence_list

def on_entry_key_release(event):
    num = get_entry_value()
    update_graph(num)

def get_entry_value():
    try:
        return int(num_entry.get())
    except ValueError:
        return 1  # Default to 1 if input is not a valid integer
def collatz_sequence(num):
    sequence_list = [num]
    while num != 1:
        if num % 2 == 0:
            num //= 2
        else:
            num = num * 3 + 1
        sequence_list.append(num)
    return sequence_list

def on_entry_key_release(event):
    num = get_entry_value()
    update_graph(num)

def get_entry_value():
    try:
        return int(num_entry.get())
    except ValueError:
        return 1  # Default to 1 if input is not a valid integer

def update_graph(num):
    sequence_list = collatz_sequence(num)

    ax.clear()
    ax.plot(sequence_list, marker='X', linestyle='dashed', markersize=4, color = "red")
    ax.set_title('Collatz Conjecture Sequence')
    ax.set_xlabel('Steps', color = 'orange')
    ax.set_ylabel('Numbers', color = "orange")
    ax.grid(True, color ="gray")

    canvas.draw()

def draw_tkinter_graph():
    root = tk.Tk()
    root.title('Collatz Conjecture Sequence')

    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    label = tk.Label(frame, text='Enter a number:')
    label.grid(row=0, column=0)

    global num_entry
    num_entry = tk.Entry(frame)
    num_entry.grid(row=0, column=1)

    # Bind the KeyRelease event to the Entry widget
    num_entry.bind("<KeyRelease>", on_entry_key_release)

    draw_button = tk.Button(frame, text='Draw Graph', command=lambda: update_graph(get_entry_value()))
    draw_button.grid(row=0, column=2)

    global fig, ax, canvas
    fig, ax = plt.subplots()
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.pack()

    root.mainloop()

if __name__ == "__main__":
    draw_tkinter_graph()
