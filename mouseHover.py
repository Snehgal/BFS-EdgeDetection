import cv2

# Mouse callback function to capture mouse position
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        print(f"Mouse Coordinates: ({x}, {y})")

def main(image_path):
    # Read the image
    image = cv2.imread(image_path)
    
    # Display the image
    cv2.imshow("Image", image)
    
    # Set the mouse callback function to track mouse position
    cv2.setMouseCallback("Image", mouse_callback)
    
    # Wait until any key is pressed to close the window
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Path to the image
    image_path = "D:/Chirag/IIITD/DM_Project/image6.png"
    
    # Run the program
    main(image_path)
