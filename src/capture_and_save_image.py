import cv2
import matplotlib.pyplot as plt

def capture_and_save_image():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        # Convert the image to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Save the image
        image_path = '/content/captured_image.jpg'
        cv2.imwrite(image_path, gray)

        # Display the captured image
        plt.imshow(gray, cmap='gray')
        plt.title('Captured Image')
        plt.axis('off')
        plt.show()
    else:
        print("Failed to capture image")

    cap.release()
