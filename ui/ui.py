import requests
from dotenv import load_dotenv, set_key
import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox, Label
from PIL import Image, ImageTk  # Import from Pillow for handling images
from get_token import get_token
from elevate_token import elevate_token


def on_get_token_button_click(status_label_get):
    # Function now takes the status_label as an argument
    try:
        get_token()
        status_label_get.config(text="Token obtained successfully!", bootstyle="success")
        messagebox.showinfo("Success", "Token obtained successfully!")  # Show pop-up message - optional
    except Exception as e:
        messagebox.showerror("Error", str(e))
        status_label_get.config(text="Error occurred", bootstyle="danger")

def on_elevate_token_button_click(status_label_elevate):
    try:
        elevate_token()  # Call the elevate_token function
        status_label_elevate.config(text="Token elevated successfully!", bootstyle="success")
        messagebox.showinfo("Success", "Token elevated successfully!")  # Show pop-up message - optional
    except Exception as e:
        messagebox.showerror("Error", str(e))
        status_label_elevate.config(text="Error occurred", bootstyle="danger")

def create_ui():
    # Create the ttkbootstrap window
    root = ttk.Window(themename="darkly")
    root.title("DBE O2 Assistant Bot")

        # Define the ASCII header
    ascii_header = """\
  ____   ___  _______ _______ 
 / __ \ / _ \|__   __/ ____|
| |__| | | | |  | | | (___  
|  __  | | | |  | |  \___ \ 
| |__| | |_| |  | |  ____) |
 \____/ \___/   |_| |_____/ 
"""

    # Create and place the ASCII header label
    header_label = ttk.Label(root, text=ascii_header, font=("Courier", 16), bootstyle="info", anchor="center", justify="center")
    header_label.grid(row=0, column=0, columnspan=2, pady=10)

    # Create and place "Get Token" button
    get_token_button = ttk.Button(root, text="Get Token", bootstyle=SUCCESS, command=lambda: on_get_token_button_click(status_label_get), width=20)
    get_token_button.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    # Create and place "Elevate Token" button
    elevate_token_button = ttk.Button(root, text="Elevate Token", bootstyle=SUCCESS, command=lambda: on_elevate_token_button_click(status_label_elevate), width=20)
    elevate_token_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    # Create status labels
    status_label_get = ttk.Label(root, text="Status: Getting Token...", bootstyle="info")
    status_label_get.grid(row=2, column=0, padx=10, pady=5, sticky="w")

    status_label_elevate = ttk.Label(root, text="Status: Elevating Token...", bootstyle="info")
    status_label_elevate.grid(row=2, column=1, padx=10, pady=5, sticky="w")

    # Load and display the cat image
    image_path = "photos/cat.jpg"  # Path to your cat image
    image = Image.open(image_path)
    image = image.resize((200, 200), Image.LANCZOS)  # Use Image.LANCZOS for high-quality resizing

    # Convert the image to a format compatible with Tkinter
    tk_image = ImageTk.PhotoImage(image)

    # Store a reference to the image to prevent garbage collection
    root.tk_image = tk_image

    # Create and place the image label
    image_label = Label(root, image=tk_image)
    image_label.grid(row=8, column=2, columnspan=2, pady=10)

    # Set window size
    root.geometry("600x800")

    return root


