import tkinter as tk
from tkinter import messagebox
from bezier import *
from PIL import Image, ImageTk


entry_points = None
entry_iterations = None
input_points = []


def create_input(frame, label, row, column):
    label = tk.Label(frame, text=label, bg="#f9e9f3", anchor='center', justify='center')
    label.grid(row=row, column=column, padx=5, pady=5, sticky='w')
    entry = tk.Entry(frame, justify='center')
    entry.grid(row=row, column=column+1, sticky='e')
    return entry


def generate_bezier_curve():
    try:
        n = int(entry_points.get())
        points = []
        for i in range(n):
            points.append(tuple(map(float, input_points[i].get().split())))
        iterations = int(entry_iterations.get())

        show_kurva_bezier(points, iterations, t=0.5, dnc=True)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def main_display():
    global entry_points, entry_iterations, input_points

    background_label.destroy()
    start_button.destroy()

    root.configure(background="#f9e9f3")

    label_title = tk.Label(root, text="Bézier Curve Generator", font=(16), pady=20, padx=20, bg="#f9e9f3", anchor='center', justify='center')
    label_title.pack()

    frame = tk.Frame(root, padx=20, pady=20, bg="#f9e9f3")
    frame.pack()

    label_points = tk.Label(frame, text="Number of points (minimum 2):", bg="#f9e9f3", anchor='center', justify='center')
    label_points.grid(row=0, column=0)
    entry_points = tk.Entry(frame, justify='center')
    entry_points.grid(row=0, column=1)

    input_points.clear()

    def create_entry_points():
        num_points = int(entry_points.get())
        for widget in input_points:
            widget.destroy()
        input_points.clear()
        for i in range(num_points):
            if i == 0:
                entry = create_input(frame, "Start Point:", i+1, 0)
            elif i == num_points - 1:
                entry = create_input(frame, "Final Point:", i+1, 0)
            else:
                entry = create_input(frame, f"Control Point {i}:", i+1, 0)
            input_points.append(entry)

    entry_points.bind("<FocusOut>", lambda event: create_entry_points())

    entry_iterations = create_input(frame, "Number of Iteration:", 20, 0)

    show_button = tk.Button(frame, text="Show the Bézier Curve", command=generate_bezier_curve, width=20, height=2, bg="#cc98aa")
    show_button.grid(row=100, column=0, columnspan=2, pady=10)


# Initial display
root = tk.Tk()
root.title("Bézier Curve Generator")
background_image = Image.open("assets/background.png")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
root.geometry("1280x720")


# Main display
start_button = tk.Button(root, text="Let's make bezier curve!", command=main_display, width=20, height=2, bg="#cc98aa")
start_button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)

root.mainloop()