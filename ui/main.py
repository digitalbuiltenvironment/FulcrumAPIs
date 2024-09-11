import requests
from dotenv import load_dotenv, set_key
import os
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox, Label
from PIL import Image, ImageTk  # Import from Pillow for handling images

def elevate_token():
    load_dotenv(override=True)

    # Base URL currently points to PROD, can be changed
    base_url = "https://optimus.fulcrumhq.build"
    endpoint = "/api/TokenAuth/Authenticate"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        "Authorization": f"Bearer {os.getenv('ACCESS_TOKEN')}"
    }

    payload = {
        "userNameOrEmailAddress": os.getenv('SVC_USERNAME'),
        'password': os.getenv('SVC_PASSWORD'),
        "rememberClient": False,
        "twoFactorRememberClientToken": None,
        "singleSignIn": False,
        "returnUrl": None,
    }

    response = requests.post(base_url + endpoint, headers=headers, json=payload)
    print(response.status_code)

    if response.status_code != 200:
        messagebox.showerror("Error", response.json()["error"]["message"])
        return
    
    print("Elevate Token successful")

    try:
        response_json = response.json()
        access_token = response_json.get("result", {}).get("accessToken")
        
        if access_token:
            print(f"Access Token: {access_token}")
            set_key(".env", "ELEVATE_TOKEN", access_token)
            messagebox.showinfo("Success", "Token elevated successfully!")
        else:
            messagebox.showwarning("Warning", "Access token not found in the response.")
    except ValueError as e:
        messagebox.showerror("Error", f"Failed to parse JSON response: {e}")

def on_button_click():
    try:
        elevate_token()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the ttkbootstrap window
root = ttk.Window(themename="darkly")
root.title("Elevate Token")

# Create and place the button
elevate_button = ttk.Button(root, text="Elevate Token", bootstyle=SUCCESS, command=on_button_click, width=20)
elevate_button.pack(pady=20)

# Load and display the cat image
image_path = "cat.jpg"  # Path to your cat image
image = Image.open(image_path)
image = image.resize((150, 150), Image.LANCZOS)  # Use Image.LANCZOS for high-quality resizing

# Convert the image to a format compatible with Tkinter
tk_image = ImageTk.PhotoImage(image)

# Create and place the image label
image_label = Label(root, image=tk_image)
image_label.pack(pady=10)

# Set window size
root.geometry("300x350")

# Run the Tkinter event loop
root.mainloop()
