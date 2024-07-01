import unittest
from src.capture_and_save_image import capture_and_save_image

class TestCaptureAndSaveImage(unittest.TestCase):
    def test_capture_and_save_image(self):
        # We can't capture and display an image in a unit test,
        # but we can test if the function runs without errors.
        try:
            capture_and_save_image()
            self.assertTrue(True)
        except Exception as e:
            self.assertTrue(False, f"Function raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()
