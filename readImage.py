import pytesseract
from PIL import Image

# Configure the path to tesseract if it's not in the PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Open an image using Pillow
image_path = r'C:\Users\Dell\Pictures\Saved Pictures\downloads\file_1.jpg'
img = Image.open(image_path)

# Define the bounding boxes (x, y, width, height) of the areas to extract
# These coordinates might need to be adjusted for your specific images
#transaction_id_box = (left_x, top_y, right_x, bottom_y)  # Replace with actual values
time_box = (120, 54, 424, 85)  # Example coordinates
amount_box = (600, 198, 683, 234)  # Example coordinates
transaction_id_box = (36, 650, 500, 700)  # Example coordinates


# Crop the image to the defined boxes
time_img = img.crop(time_box)
amount_img = img.crop(amount_box)
transaction_id_img = img.crop(transaction_id_box)

# Use Tesseract to do OCR on the cropped images
time_text = pytesseract.image_to_string(time_img, lang='eng')
amount_text = pytesseract.image_to_string(amount_img, lang='eng')
transaction_id_text = pytesseract.image_to_string(transaction_id_img, lang='eng')

# Clean the extracted text
time_text = time_text.strip()
amount_text = amount_text.strip().replace('₹', '').strip()  # Remove the currency symbol if present
transaction_id_text = transaction_id_text.strip()

# Output the data
print(f"Time: {time_text}")
print(f"Amount: {amount_text}")
print(f"Transaction ID: {transaction_id_text}")
