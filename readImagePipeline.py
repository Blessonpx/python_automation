import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

# Configure the path to tesseract if it's not in the PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# 0- List all the files in a folder
# 1- Read the header if it is a `Paid to` or `Recieved`
# 2- If Paid,then catch reciever credentials
# 3- If recieved then catch credentials
# Open an image using Pillow

#id_box = (left_x, top_y, right_x, bottom_y)  # Replace with actual values
class InputImage:
    def __init__(self,image_path):
        self.img = Image.open(image_path)
    def find_category(self):
        category_box = (15, 15, 693, 303)
        category_img = self.img.crop(category_box)
        category_text = pytesseract.image_to_string(category_img, lang='eng')
        category_text = category_text.strip()
        if "Received from" in category_text:
            return "Recieved"
        if "Paid to" in category_text:
            return "PaidTo"
        return "NA"
    def find_name(self):
        detail_box = (134,202,680,286)
        detail_img = self.img.crop(detail_box)
        #detail_text = pytesseract.image_to_string(detail_img, lang='eng')
        #detail_text = detail_text.strip().replace('₹', '').strip()
        detail_img = detail_img.convert('L')
        #detail_img = detail_img.point(lambda x: 0 if x < 140 else 255, '1')  # Threshold
        detail_img = detail_img.filter(ImageFilter.SHARPEN)  # Sharpen the image
        #detail_img = detail_img.resize([2 * s for s in detail_img.size], Image.BICUBIC)  # Scale up
        custom_config = r'--oem 3 --psm 6 -c tessedit_char_whitelist=0123456789,.'
        detail_text = pytesseract.image_to_string(detail_img, lang='eng', config=custom_config)
        detail_text = detail_text.strip()
        return f"{detail_text}"


#Coordinates: 134, 202
#Coordinates: 680, 286
        return f"{detail_text}"
    def find_amount(self):
        detail_box =  (134,202,680,286)
        detail_img = self.img.crop(detail_box)
        detail_text = pytesseract.image_to_string(detail_img, lang='eng')
        detail_text = detail_text.strip().replace('₹', '').strip()
        return f"{detail_text}"
if __name__=='__main__':
    image_path = r'C:\Users\Dell\Pictures\Saved Pictures\downloads\file_4.jpg'
    x=InputImage(image_path)
    print(x.find_category())
    print(x.find_name())
    print(x.find_amount())
    