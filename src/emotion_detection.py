import cv2
import numpy as np
import time

# Example emotion dictionary
emotion_dict = {0: "Angry", 1: "Disgust", 2: "Fear", 3: "Happy", 4: "Sad", 5: "Surprise", 6: "Neutral"}

def emotion_detection(image):
    # Resize the image to 48x48
    resized_image = cv2.resize(image, (48, 48), interpolation=cv2.INTER_AREA)
    
    # Reshape for 4D convolution input to model
    reshaped_resized_image = np.reshape(resized_image, [1, 48, 48, 1])
    
    # Do the prediction based on the emotional model
    start_time = time.time()
    predicted_class = np.argmax(model.predict(reshaped_resized_image))
    elapsed_time = time.time() - start_time
    print(f'Elapsed Model Run Time: {elapsed_time:.3f} seconds')
    
    # Get the emotion string from the dictionary with predicted class as index
    label_map = {v: k for k, v in emotion_dict.items()}
    predicted_label = label_map[predicted_class]
    
    # Return the emotion string
    return predicted_label, elapsed_time
