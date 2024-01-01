import pytesseract
from PIL import Image

# Configure the path to tesseract if it's not in the PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 0- List all the files in a folder
# 1- Read the header if it is a `Paid to` or `Recieved`
# 2- If Paid,then catch reciever credentials
# 3- If recieved then catch credentials
# Open an image using Pillow


class InputImage:
    def __init__(self):
        self.image=None
    def find_category(self,image_path):
        img = Image.open(image_path)
        category_box = (15, 15, 693, 303)
        category_img = img.crop(category_box)
        category_text = pytesseract.image_to_string(category_img, lang='eng')
        category_text = category_text.strip()
        if "Received from" in category_text:
            return "Recieved"
        if "Paid to" in category_text:
            return "Paid"
        return "NA"

if __name__=='__main__':
    image_path = r'C:\Users\Dell\Pictures\Saved Pictures\downloads\file_1.jpg'
    x=InputImage()
    print(x.find_category(image_path))