import cv2

# Function to display the image
def show_image(winname, img):
    cv2.imshow(winname, img)
    cv2.moveWindow(winname, 500, 0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Callback function to get coordinates on mouse click
def get_coordinates(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(f"Coordinates: {x}, {y}")

# Load your image
image_path = r'C:\Users\Dell\Pictures\Saved Pictures\downloads\file_1.jpg'
image = cv2.imread(image_path)


# Show the image and wait for a click
cv2.namedWindow('Image')
cv2.setMouseCallback('Image', get_coordinates)
show_image('Image', image)
