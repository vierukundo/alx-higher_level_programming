#!/usr/bin/python3
# base.py
"""definition of base class"""
import json
import csv


class Base:
    """represents base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialization of class instances
        args:
            id(int or None): id of object
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        filename = str(cls.__name__) + ".json"
        with open(filename, 'w', encoding="utf-8") as f:
            if list_objs is None:
                f.write(cls.to_json_string([]))
            else:
                objs_dictionary = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(objs_dictionary))

    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == 'Rectangle':
            dummy = cls(2, 3, 5)
        elif cls.__name__ == 'Square':
            dummy = cls(2)
        else:
            raise ValueError("Invalid subclass")
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as f:
                dicts_list = json.load(f)
                if dicts_list is None:
                    return []
                instances_list = []
                for obj_dict in dicts_list:
                    if isinstance(obj_dict, dict):
                        instance = cls.create(**obj_dict)
                        instances_list.append(instance)
                return instances_list
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """writes the csv string representation of list_objs to a file"""
        filename = str(cls.__name__) + ".csv"
        with open(filename, 'w', newline='') as csv_f:
            if cls.__name__ == "Rectangle":
                fieldnames = ['id', 'width', 'height', 'x', 'y']
            else:
                fieldnames = ['id', 'size', 'x', 'y']
            writer = csv.DictWriter(csv_f, fieldnames=fieldnames)
            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""
        filename = str(cls.__name__) + ".csv"
        instances_list = []
        try:
            with open(filename, 'r', newline='') as csv_f:
                reader = csv.DictReader(csv_f)
                for row in reader:
                    if cls.__name__ == "Rectangle":
                        instance = cls.create(id=int(row['id']), width=int(
                            row['width']), height=int(row['height']), x=int(
                                row['x']), y=int(row['y']))
                    elif cls.__name__ == "Square":
                        instance = cls.create(id=int(row['id']), size=int(
                            row['size']), x=int(row['x']), y=int(row['y']))
                    else:
                        raise ValueError("Base has no given subclass")
                    instances_list.append(instance)
        except FileNotFoundError:
            pass
        return instances_list
