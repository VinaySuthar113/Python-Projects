import customtkinter as ctk
from tkinter import colorchooser, messagebox
import json
import random
from PIL import Image

# Function to calculate the average color
def average_colors(colors):
    avg_color = [sum(x) / len(x) for x in zip(*colors)]
    return tuple(map(int, avg_color))

# Function to choose a color
def choose_color():
    color_code = colorchooser.askcolor(title="Choose a color")
    
    if color_code:
        rgb_color = color_code[0]  # The RGB value
        hex_color = color_code[1]  # The hexadecimal value
        
        if rgb_color:
            colors.append((rgb_color, hex_color))
            update_display()

def save_colors():
    if colors:
        with open('saved_colors.json', 'w') as file:
            json.dump(colors, file)
        messagebox.showinfo("Saved", "Colors saved successfully.")
    else:
        messagebox.showwarning("Empty", "No colors to save.")

def load_colors():
    global colors
    try:
        with open('saved_colors.json', 'r') as file:
            colors = json.load(file)
        update_display()
        messagebox.showinfo("Loaded", "Colors loaded successfully.")
    except FileNotFoundError:
        messagebox.showinfo("Error", "No saved colors found.")

def remove_color(index):
    confirm = messagebox.askyesno("Confirm", "Are you sure you want to remove this color?")
    if confirm:
        del colors[index]
        update_display()
        messagebox.showinfo("Removed", "Color removed successfully.")

def generate_random_combo():
    colors.clear()
    for _ in range(3):  # Generate 3 random colors
        rgb_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        hex_color = '#%02x%02x%02x' % rgb_color
        colors.append((rgb_color, hex_color))
    update_display()

def update_display():
    # Clear the color frames
    for frame in color_frames:
        frame.destroy()
    color_frames.clear()
    
    # Display chosen colors
    for index, (rgb_color, hex_color) in enumerate(colors, start=1):
        color_text = f"Color {index}: {rgb_color}\nHex: {hex_color}"
        frame = ctk.CTkFrame(color_frame_container, fg_color=hex_color, bg_color='#ffffff')  # Light background
        label = ctk.CTkLabel(frame, text=color_text, text_color="black")  # Black text
        label.pack(pady=10, padx=10, side='left')
        
        remove_button = ctk.CTkButton(frame, text="Remove", command=lambda idx=index-1: remove_color(idx), bg_color='#333333', hover_color='#b37c52',fg_color = '#2aa687')  # Darker button colors
        remove_button.pack(pady=10, padx=10, side='right')
        
        frame.pack(pady=10, padx=5, fill='x', expand=True)
        color_frames.append(frame)
    
    # Calculate and display the combined color if there are multiple colors
    if len(colors) > 1:
        rgb_values = [color[0] for color in colors]
        combined_color = average_colors(rgb_values)
        combined_hex = '#%02x%02x%02x' % combined_color
        combined_color_text = f"Combined RGB: {combined_color}\nCombined Hex: {combined_hex}"
        
        # Destroy the previous combined color frame if it exists
        if hasattr(update_display, 'combined_color_frame'):
            update_display.combined_color_frame.destroy()
        
        combined_color_frame = ctk.CTkFrame(root, fg_color=combined_hex, bg_color='#ffffff')  # Light background
        combined_color_label = ctk.CTkLabel(combined_color_frame, text=combined_color_text, text_color="black")  # Black text
        combined_color_label.pack(pady=10, padx=10)
        combined_color_frame.pack(pady=20, fill='x', expand=True)
        
        # Store the new combined color frame reference
        update_display.combined_color_frame = combined_color_frame
        
        # Show the guideline only if more than two colors are chosen
        if len(colors) > 2:
            combined_label.configure(text="Choose color to combine")
    else:
        combined_label.configure(text="Choose first color to combine")

# Initialize main window
root = ctk.CTk()
root.geometry("400x600")
root.resizable(False, False)  # False resize for the window
root.configure(bg='#000000')  # dark background for the entire window

colors = []
color_frames = []


# Main Image at the side
image_path = "D://PythonProjects//TkinterProjects//badass1.jpg"
loaded_image = ctk.CTkImage(Image.open(image_path), size=(400, 600))
background_label = ctk.CTkLabel(master=root, image=loaded_image, text="")
background_label.place(y=0, x=0)

# Button to choose color
choose_color_button = ctk.CTkButton(root, text="Choose Color", command=choose_color, bg_color='black', fg_color='#5278b1')  # Custom button colors
choose_color_button.pack(pady=10, padx=10, fill='x', expand=True)

# Frame to hold color frames with a scrollable area
color_frame_container = ctk.CTkScrollableFrame(root, bg_color='black')  # Light background
color_frame_container.pack(pady=10, padx=10, fill='both', expand=True)

# Label to display the guideline
combined_label = ctk.CTkLabel(root, text="Choose first color to combine", bg_color='#ffffcc', text_color='#000000')  # Custom label colors
combined_label.pack(padx=10, fill='x', expand=True)

# Button to save colors
save_button = ctk.CTkButton(root, text="Save Colors", command=save_colors, bg_color='black', fg_color='#85509b', hover_color = '#7c9c64')  # Darker button colors
save_button.pack(padx=10, fill='x', expand=True)

# Button to load saved colors
load_button = ctk.CTkButton(root, text="Load Colors", command=load_colors, bg_color='black', fg_color='#85509b', hover_color = '#7c9c64')  # Darker button colors
load_button.pack(padx=10, fill='x', expand=True)

# Button to generate random color combination
random_combo_button = ctk.CTkButton(root, text="Generate Random Combo", command=generate_random_combo, bg_color='#7c9c64', fg_color='#85509b', hover_color = '#7c9c64')  # Darker button colors
random_combo_button.pack(padx=10, fill='x', expand=True)

# Run the main event loop
root.mainloop()
