import unittest
import tensorflow as tf
from src.emotion_detection import train_generator, validation_generator

class TestEmotionDetection(unittest.TestCase):
    def test_data_generators(self):
        self.assertIsNotNone(train_generator)
        self.assertIsNotNone(validation_generator)

if __name__ == '__main__':
    unittest.main()
