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
        if n < 2:
            raise ValueError("Number of points must be at least 2.")
        
        points = []
        for i in range(n):
            point_str = input_points[i].get().strip()
            if not point_str:
                raise ValueError(f"Point {i+1} is empty.")
            point = tuple(map(float, point_str.split()))
            if len(point) != 2:
                raise ValueError(f"Invalid format for point {i+1}. Points should be separated by space.")
            points.append(point)
        
        iterations = int(entry_iterations.get())
        if iterations < 0:
            raise ValueError("Number of iterations must be at least 0.")

        show_kurva_bezier(points, iterations, t=0.5, dnc=True)
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", str(e))


def back_to_initial_display():
    global background_label, start_button, back_button

    label_title.destroy()
    frame.destroy()
    entry_points.destroy()
    entry_iterations.destroy()
    show_button.destroy()
    back_button.destroy()

    background_label = tk.Label(root, image=background_photo)
    background_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
    start_button = tk.Button(root, text="Let's Make Bézier Curve!", command=main_display, width=20, height=2, bg="#cc98aa")
    start_button.place(relx=0.5, rely=0.75, anchor=tk.CENTER)


def main_display():
    global entry_points, entry_iterations, input_points, label_title, frame, show_button, back_button

    # Hide initial display widgets
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
        try:
            num_points = int(entry_points.get())
            if num_points < 2:
                messagebox.showerror("Error", "Number of points must be at least 2.")
                return
            for widget in input_points:
                widget.destroy()
            input_points.clear()
            for i in range(num_points):
                if i == 0:
                    entry = create_input(frame, "Start Point:", i + 1, 0)
                elif i == num_points - 1:
                    entry = create_input(frame, "Final Point:", i + 1, 0)
                else:
                    entry = create_input(frame, f"Control Point {i}:", i + 1, 0)
                input_points.append(entry)
        except ValueError:
            messagebox.showerror("Error", "Invalid input for number of points.")

    entry_points.bind("<FocusOut>", lambda event: create_entry_points())

    entry_iterations = create_input(frame, "Number of Iteration:", 20, 0)

    show_button = tk.Button(frame, text="Show the Bézier Curve", command=generate_bezier_curve, width=20, height=2, bg="#cc98aa")
    show_button.grid(row=100, column=0, columnspan=2, pady=10)
    back_button = tk.Button(root, text="\u2190", font=('Arial', 12), command=back_to_initial_display, width=3, height=1, bg="#cc98aa")
    back_button.place(relx=0, rely=0, anchor=tk.NW)


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