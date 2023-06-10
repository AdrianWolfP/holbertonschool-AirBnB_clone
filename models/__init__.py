#!/usr/bin/python3
"""Module creates a unique FileStorage instance for your application"""

from models.engine.file_storage import FilesStorage
from models.base_model import BaseModel

storage = FileStorage()
storage.reload()