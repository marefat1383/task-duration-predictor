import unittest

from task_duration import predict_hours


class TaskDurationTests(unittest.TestCase):
    def test_prediction_is_positive(self):
        self.assertGreater(predict_hours(7, 3, 2), 0)

    def test_invalid_complexity_is_rejected(self):
        with self.assertRaises(ValueError):
            predict_hours(11, 3, 2)


if __name__ == "__main__":
    unittest.main()
