#!/usr/bin/python3
"""Base model class"""
import uuid
import datetime
from models import storage


class BaseModel():
    """The base class from which other classes inherit from"""

    def __init__(self, *args, **kwargs):
        """Innitializes base class attributes"""

        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)
        else:
            for key in kwargs.keys():
                # check and skip the __class__ key
                if key == "__class__":
                    continue
                else:
                    # format the updated_at & created_at
                    if key == "updated_at" or key == "created_at":
                        kwargs[key] = datetime.datetime.strptime(
                            kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                    # sest instance attribute
                    setattr(self, key, kwargs[key])
                # self.key = kwargs[key]
                # print(f"{key}: {kwargs[key]}")

    def __str__(self):
        """Returns the resulting string rep"""
        return (f"[{self.__class__.__name__}] ({self.id}) \
{str(self.__dict__)}")

    def save(self):
        """updates the updated_at attribute"""
        storage.save()
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Reaturns the key/value attributes"""
        object_dict = {}
        for key in self.__dict__.keys():
            if key not in ('created_at', 'updated_at'):
                object_dict[key] = self.__dict__[key]
            else:
                object_dict[key] = datetime.datetime.isoformat(
                    self.__dict__[key])
        object_dict['__class__'] = self.__class__.__name__
        return (object_dict)
