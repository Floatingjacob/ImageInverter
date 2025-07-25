import os
from PIL import Image
from PIL import ImageOps
import platform

def invert_image(filepath):
    try:
# Make an output folder called 'inverted' if it does not already exist
        os.makedirs("inverted", exist_ok = True)
        
# Remove quotation marks and then makes the path a string incase it has spaces
        stripchars = ['"', '\'']
        for i in stripchars:
            filepath = f'{filepath.replace(i, "")}'
            
        # Check if file exists
        if not os.path.exists(filepath):
            print(f"Error: File '{filepath}' does not exist.")
            return

        # Open the image
        img = Image.open(filepath)
        
        # Convert to RGB if necessary (handles PNG with transparency, etc.)
        if img.mode in ('RGBA', 'LA'):
            img = img.convert('RGB')
            
        # Invert the colors
        inverted_img = ImageOps.invert(img)
        
        # Get the original filename and create new filename
        filename = os.path.basename(filepath)
        name, ext = os.path.splitext(filename)
        new_filename = f"{name}_inverted{ext}"

        save_path = os.path.join("inverted", new_filename)
        
        # Save the inverted image
        inverted_img.save(save_path)
        print(f"Inverted image saved as: {os.path.abspath(save_path)}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Prompt user for filepath
    filepath = input("Please enter the image filepath: ")
    invert_image(filepath)
