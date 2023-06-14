<<<<<<< HEAD
#!/usr/bin/python3
"""
Amenity class module
"""

from models.base_model import BaseModel
from datetime import datetime


class Amenity(BaseModel):
    """Defines Amenity class"""

    def __init__(self, *args, **kwargs):
        """Initializes instances"""
        if kwargs:
            kwargs.pop("__class__", None)
            if "created_at" in kwargs:
                kwargs['created_at'] = datetime.strptime(
                    kwargs['created_at'], self.timeformat)
            if "updated_at" in kwargs:
                kwargs['updated_at'] = datetime.strptime(
                    kwargs['updated_at'], self.timeformat)
            super().__init__(*args, **kwargs)
        else:
            super().__init__(*args, **kwargs)
=======
#!
>>>>>>> f316a631296f42a2d78156d9c26119fa1cae2e76
