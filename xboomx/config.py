import os
import json
import logging

config_dir = os.path.join(os.getenv("HOME"), '.config', 'xboomx')

def load_config():
    try:
        with open(os.path.join(config_dir, "config")) as config_file:
            return json.loads('\n'.join(config_file.readlines()))
    except:
        logging.error(f"Failed to load config file at {config_dir}")
        return {}


config = load_config()
