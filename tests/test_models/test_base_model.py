#!/usr/bin/python3
"""
Base model test
"""
import unittest
import time
from datetime import datetime
from unittest import mock
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test Case For Base Model
    """

    def test_instance_creation(self):
        """
        Test instance creation and attribute assignment
        """
        instance = BaseModel()
        self.assertIsInstance(instance, BaseModel)
        instance.name = "Ahmed"
        instance.phone = 9525
        type_attr = {
            "id": str,
            "updated_at": datetime,
            "created_at": datetime,
            "name": str,
            "phone": int
        }
        for attr, type_at in type_attr.items():
            with self.subTest(attr=attr, typ=type_at):
                self.assertIn(attr, instance.__dict__)
                self.assertIsInstance(instance.__dict__[attr], type_at)
        self.assertTrue(mock_storage.new_called)
        self.assertEqual(instance.name, "Ahmed")
        self.assertEqual(instance.phone, 9525)

    def test_datetime(self):
        """
        Test different instance, different time,
        same created_at and updated_at when
        instance is created
        """
        tc_before = datetime.now()
        instance1 = BaseModel()
        tc_after = datetime.now()
        self.assertTrue(tc_before <= instance1.created_at <= tc_after)
        time.sleep(1e-4)
        instance2 = BaseModel()
        self.assertEqual(instance1.created_at, instance1.updated_at)
        self.assertNotEqual(instance1.created_at, instance2.created_at)
        self.assertNotEqual(instance1.updated_at, instance2.updated_at)

    def test_uuid(self):
        """
        Test different uuid for different instances
        """
        instance1 = BaseModel()
        instance2 = BaseModel()
        self.assertNotEqual(instance1.id, instance2.id)
        uuid_value = instance1.id
        with self.subTest(uuid=uuid_value):
            self.assertIsInstance(uuid_value, str)

    def test_to_dict(self):
        """
        Test to_dict method in BaseModel
        """
        instance = BaseModel()
        instance.name = "ahmed"
        instance.num = 95
        dict_inst = instance.to_dict()
        attributes = [
            "id",
            "created_at",
            "updated_at",
            "name",
            "num",
            "__class__"
        ]
        self.assertCountEqual(dict_inst.keys(), attributes)
        self.assertEqual(dict_inst['__class__'], 'BaseModel')
        self.assertEqual(dict_inst['name'], "ahmed")
        self.assertEqual(dict_inst['num'], 95)

    def test_to_dict_values(self):
        """
        Test that to_dict return values are correct
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        instance = BaseModel()
        dict_base = instance.to_dict()
        self.assertEqual(dict_base["__class__"], "BaseModel")
        self.assertEqual(type(dict_base["created_at"]), str)
        self.assertEqual(type(dict_base["updated_at"]), str)
        self.assertEqual(
            dict_base["created_at"],
            instance.created_at.strftime(time_format)
        )
        self.assertEqual(
            dict_base["updated_at"],
            instance.updated_at.strftime(time_format)
        )

    def test_str(self):
        """
        Test str method
        """
        instance = BaseModel()
        correct_str = "[BaseModel] ({}) {}".format(
            instance.id,
            instance.__dict__
        )
        self.assertEqual(correct_str, str(instance))

    @mock.patch("models.storage")
    def test_save(self, mock_storage):
        """
        Test save, update_at, and check if storage.save is called
        """
        instance = BaseModel()
        old_value_created = instance.created_at
        old_value_updated = instance.updated_at
        instance.save()
        new_value_created = instance.created_at
        new_value_updated = instance.updated_at
        self.assertNotEqual(old_value_updated, new_value_updated)
        self.assertEqual(old_value_created, new_value_created)
        self.assertTrue(mock_storage.save.called)
