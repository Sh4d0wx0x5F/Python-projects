import tkinter as tk
from tkinter import messagebox

# Create the main window
window = tk.Tk()
window.withdraw()  # Hide the main window

# Display an information box
messagebox.askyesno("Information", "This is an information box.")

# Start the main window's event loop
window.mainloop()
