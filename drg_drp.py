import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
import shutil
import os

# Create a TkinterDnD window
root = TkinterDnD.Tk()
root.title("Drag & Drop Excel File")
root.geometry("400x200")

# Label for instructions
label = tk.Label(root, text="Drag and drop an Excel file here", fg="blue", font=("Arial", 12))
label.pack(pady=20)

# Function to handle file drop
def drop(event):
    file_path = event.data.strip('{}')  # Handle Windows-style paths
    if file_path.endswith(('.xlsx', '.xls')):  # Ensure it's an Excel file
        file_name = os.path.basename(file_path)
        destination = os.path.join(os.getcwd(), file_name)  # Save in current directory

        try:
            shutil.copy(file_path, destination)
            label.config(text=f"File saved: {file_name}", fg="green")
        except Exception as e:
            label.config(text=f"Error: {e}", fg="red")
    else:
        label.config(text="Invalid file type! Drop an Excel file.", fg="red")

# Make the window a drop target
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

# Run the Tkinter event loop
root.mainloop()
