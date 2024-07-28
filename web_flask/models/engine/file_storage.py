import json
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for obj in obj_dict.values():
                    cls_name = obj['__class__']
                    del obj['__class__']
                    self.__objects[cls_name] = eval(cls_name)(**obj)
        except FileNotFoundError:
            pass

    def close(self):
        self.reload()
