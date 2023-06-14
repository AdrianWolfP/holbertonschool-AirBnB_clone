#!/usr/bin/python3
"""
City class module
"""


from typing import Any
from datetime import datetime
from models.base_model import BaseModel

class City(BaseModel):
    """Defines City class"""

    state_id: str = ""
    name: str = ""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initializes instances"""
        if kwargs:
            if "__class__" in kwargs:
                del kwargs["__class__"]
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     self.timeformat)
            if "updated_at" in kwargs:
                kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                         self.timeformat)
            super().__init__(*args, **kwargs)
        else:
            super().__init__(*args, **kwargs)
