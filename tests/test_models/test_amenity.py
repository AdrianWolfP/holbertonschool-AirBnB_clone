#!/usr/bin/python3
import unittest
import os
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):

    def setUp(self):
        self.amenity = Amenity()

    def tearDown(self):
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_init(self):
        self.assertIsNotNone(self.amenity)

    def test_attributes(self):
        self.assertEqual(self.amenity.name, "")
        self.assertTrue(hasattr(self.amenity, "created_at"))
        self.assertFalse(hasattr(self.amenity, "updated_at"))
        self.assertTrue(hasattr(self.amenity, "id"))
        self.amenity.save()
        self.assertTrue(hasattr(self.amenity, "updated_at"))

    def test_to_json(self):
        example_to_json = Amenity.to_json(self.amenity)
        self.assertEqual(type(example_to_json), dict)

    def test_str(self):
        example_str = "[{}] ({}) {}".format(
            self.amenity.__class__.__name__,
            self.amenity.id,
            self.amenity.__dict__
        )
        self.assertEqual(str(self.amenity), example_str)

    def test_repr(self):
        self.assertIsNotNone(self.amenity.__str__())


if __name__ == "__main__":
    unittest.main()
