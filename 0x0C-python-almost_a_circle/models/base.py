#!/usr/bin/python3
""" module contains class defination"""
import json


class Base:
    """ represent clase Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation of list_dictionaries """
        if not list_dictionaries or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file:"""
        name = cls.__name__ + ".json"
        with open(name, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                dic_list = [listt.to_dictionary() for listt in list_objs]
                f.write(Base.to_json_string(dic_list))

    @staticmethod
    def from_json_string(json_string):
        """ that returns the list of the JSON string
            representation json_string:"""
        if not json_string or json_string is None:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(10, 20, 30, 40)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances:"""
        fname = cls.__name__ + ".json"
        try:
            with open(fname, mode="r", encoding="utf-8") as jf:
                dictt = Base.from_json_string(jf.read())
                return [cls.create(**dic) for dic in dictt]
        except IOError:
            return "[]"
