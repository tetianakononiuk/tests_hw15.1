import unittest
import os
from json_operations import write_to_file, read_from_file
from text_processor import TextProcessor

class TestFileOperations(unittest.TestCase):
    def setUp(self):
        self.test_file = 'test.json'
        self.test_data = {
            "pk": 4,
            "title": "Test Title",
            "author": "Test Author",
            "published_date": "2024-06-23",
            "publisher": 6,
            "price": 9.99,
            "discounted_price": 3.56,
            "is_bestseller": True,
            "is_banned": False,
            "genres": [1, 2, 3]
        }

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_write_and_read_file(self):
        write_to_file(self.test_file, self.test_data)
        data = read_from_file(self.test_file)
        self.assertEqual(data, self.test_data)

    def test_write_and_read_empty_file(self):
        write_to_file(self.test_file, {})
        data = read_from_file(self.test_file)
        self.assertEqual(data, {})

    def test_read_nonexistent_file(self):
        with self.assertRaises(FileNotFoundError):
            read_from_file('nonexistent.json')

    def test_write_bad_data_into_file(self):
        with self.assertRaises(TypeError):
            write_to_file(self.test_file, set([1, 2, 3]))

class TestTextProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = TextProcessor("Hello, World! This is a test.")

    def test_clean_text(self):
        self.processor.clean_text()
        self.assertEqual(self.processor.cleaned_text, "hello world this is a test")

    def test_clean_text_empty_string(self):
        empty_processor = TextProcessor("")
        empty_processor.clean_text()
        self.assertEqual(empty_processor.cleaned_text, "")

    def test_remove_stop_words(self):
        stop_words = ["this", "is", "a"]
        self.processor.clean_text()
        self.processor.remove_stop_words(stop_words)
        self.assertEqual(self.processor.cleaned_text, "hello world test")

    def test_remove_stop_words_without_cleaning(self):
        stop_words = ["this", "is", "a"]
        self.processor.remove_stop_words(stop_words)
        self.assertEqual(self.processor.cleaned_text, "hello world test")

    def test_remove_stop_words_no_stop_words(self):
        stop_words = ["not", "in", "text"]
        self.processor.clean_text()
        self.processor.remove_stop_words(stop_words)
        self.assertEqual(self.processor.cleaned_text, "hello world this is a test")

if __name__ == '__main__':
    unittest.main()