import unittest
from src.emotion_detection import emotion_detection
import cv2

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        image = cv2.imread('examples/example_image.jpg')
        predicted_label, elapsed_time = emotion_detection(image)
        self.assertIsInstance(predicted_label, str)
        self.assertIsInstance(elapsed_time, float)

if __name__ == '__main__':
    unittest.main()
