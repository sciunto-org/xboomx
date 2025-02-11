import os
import json
import logging


def load_config():
    config_dir = os.path.join(os.getenv("HOME"), '.xboomx')
    try:
        with open(os.path.join(config_dir, "config")) as config_file:
            return json.loads('\n'.join(config_file.readlines()))
    except:
        logging.error("Failed to load config file")
        return {}


config = load_config()
