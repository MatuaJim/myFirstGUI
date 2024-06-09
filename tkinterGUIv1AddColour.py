import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("My First GUI by Matua Halafihi")
root.geometry("400x300")  # Set the window size to 400x300 pixels
root.config(bg="lightblue")  # Set the background color of the main window

## Functions
def show_message():
    """Display a message when the button is clicked"""
    message_label.config(text="Hello, World!", fg="white")

## Widgets
# Create a label
label = tk.Label(root, text="Welcome to my GUI! by Matua", bg="yellow", fg="black")
label.pack(pady=20)

# Create a button
button = tk.Button(root, text="Click Me", command=show_message, bg="green", fg="white")
button.pack(pady=20)

# Create a label to display the message
message_label = tk.Label(root, text="", bg="grey", fg="black")
message_label.pack(pady=20)

# Start the main event loop
root.mainloop()

