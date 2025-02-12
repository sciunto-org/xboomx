import os
import json
import logging

config_dir = os.path.join(os.getenv("HOME"), '.config', 'xboomx')
os.makedirs(config_dir, exist_ok=True)


def load_config():
    """
    Load configuration, init if doesn't exist.
    """
    config_path = os.path.join(config_dir, "config")
    default_config = {
        "dmenu_params": "-i -nb black -nf orange -sb black -p \"#\""
    }

    try:
        with open(config_path, 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        logging.warning(f"Configuration file not found at {config_path}. Creating a new one with default settings.")

        # Init configuration
        with open(config_path, 'w') as config_file:
            json.dump(default_config, config_file, indent=4)
        return default_config
    except json.JSONDecodeError:
        logging.error(f"Failed to decode JSON from the config file at {config_path}.")
        return {}
    except Exception as e:
        logging.error(f"An unexpected error occurred while loading the config file: {e}")
        return {}


config = load_config()
