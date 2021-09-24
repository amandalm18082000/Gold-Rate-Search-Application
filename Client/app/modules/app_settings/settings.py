import json
import os

# APP SETTINGS
class Settings(object):
    # APP PATH
    json_file = "settings.json"
    app_path = os.path.abspath(os.getcwd())
    settings_path = os.path.join(app_path, json_file)

    # ALL OBJECTS
    _objects = []

    def __init__(
        self,
        app_name = "",
        custom_title_bar = True,
        startup_size = [],
        minimum_size = [],
        left_menu = {            
            "color": "",
            "color_hover": "",
            "color_pressed": "",
            "icon_color": "",
            "icon_color_pressed": ""
        }
    ):
        self._objects.append(self)

        # APP SETTINGS
        self.app_name = app_name
        self.custom_title_bar = custom_title_bar
        self.startup_size = startup_size
        self.minimum_size = minimum_size

        # LEFT MENU
        self.left_menu = left_menu

    def serialize(self):
        serialize = Settings()
        with open(self.settings_path, "w", encoding='utf-8') as write:
            json.dump(serialize.__dict__, write, indent=4)

    # DESERIALIZE JSON
    def deserialize(self):
        # READ JSON FILE       
        with open(self.settings_path, "r", encoding='utf-8') as reader:
            settings = json.loads(reader.read())
            obj = Settings(**settings)
        
        # SET GLOBAL DICT
        global settings_dict
        settings_dict = obj

        # UPDATE OBJECTS VALUES
        self.app_name = obj.app_name
        self.custom_title_bar = obj.custom_title_bar
        self.startup_size = obj.startup_size
        self.minimum_size = obj.minimum_size
        self.left_menu = obj.left_menu
        

settings_dict = Settings()
settings_dict.__dict__