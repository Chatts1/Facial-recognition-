import unittest
from src.build_model import build_and_train_model, create_data_generators

class TestModel(unittest.TestCase):
    def test_build_and_train_model(self):
        train_generator, validation_generator = create_data_generators()
        model, history = build_and_train_model(train_generator, validation_generator)
        self.assertIsNotNone(model)
        self.assertIsNotNone(history)

if __name__ == '__main__':
    unittest.main()
