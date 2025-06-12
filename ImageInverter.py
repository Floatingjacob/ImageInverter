import os
from PIL import Image
from PIL import ImageOps
import platform

def get_downloads_path():
    """Get the Downloads directory path based on the operating system."""
    if platform.system() == "Windows":
        return os.path.join(os.path.expanduser("~"), "Downloads")
    else:
        return os.path.join(os.path.expanduser("~"), "Downloads")

def invert_image(filepath):
    """Invert colors of an image and save to Downloads directory."""
    try:
        # Remove quotation marks if present
        filepath = filepath.strip('"\'')
        
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
        
        # Get Downloads directory path
        downloads_path = get_downloads_path()
        save_path = os.path.join(downloads_path, new_filename)
        
        # Save the inverted image
        inverted_img.save(save_path)
        print(f"Inverted image saved as: {save_path}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Prompt user for filepath
    filepath = input("Please enter the image filepath: ")
    invert_image(filepath)