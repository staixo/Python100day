import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

# Function to add watermark to an image
def add_watermark(image_path, watermark_text):
    # Open the image
    image = Image.open(image_path)
    
    # Create a copy of the image
    watermark_image = image.copy()
    
    # Set the watermark text font and size
    watermark_font = ImageFont.truetype("/Users/henripeters/Documents/Projetperso/Python100day/Professional/Roboto-Black.ttf", 40)
    
    # Calculate the position to place the watermark (bottom-right corner)
    watermark_width, watermark_height = watermark_font.getsize(watermark_text)
    image_width, image_height = image.size
    watermark_position = (image_width - watermark_width - 10, image_height - watermark_height - 10)
    
    # Draw the watermark text on the image
    draw = ImageDraw.Draw(watermark_image)
    draw.text(watermark_position, watermark_text, fill=(255, 255, 255), font=watermark_font)
    
    # Save the watermarked image
    watermarked_image_path =  image_path.split(".")[0] + "_watermarked.jpg"
    watermark_image.save(watermarked_image_path)
    
    # Show a success message
    result_label.config(text="Watermark added successfully!")
    
    # Open the watermarked image
    watermarked_image = Image.open(watermarked_image_path)
    watermarked_image.show()

# Function to handle button click event
def upload_image():
    # Prompt the user to select an image file
    file_path = filedialog.askopenfilename(filetypes=[("JPEG Files", "*.jpg"), ("PNG Files", "*.png"), ("GIF Files", "*.gif")])
    
    # Check if a file was selected
    if file_path:
        # Reset the result label text
        result_label.config(text="")
        
        # Add watermark to the selected image
        add_watermark(file_path, watermark_entry.get())

# Create the main window
window = tk.Tk()
window.title("Image Watermarking")
window.geometry("300x150")

# Create and place the watermark label and entry
watermark_label = tk.Label(window, text="Watermark:")
watermark_label.pack()
watermark_entry = tk.Entry(window)
watermark_entry.pack()

# Create and place the upload button
upload_button = tk.Button(window, text="Upload Image", command=upload_image)
upload_button.pack()

# Create and place the result label
result_label = tk.Label(window, text="")
result_label.pack()

# Start the main event loop
window.mainloop()
