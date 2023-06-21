import configparser

config = configparser.ConfigParser()
config.read("config.txt")
api_key = config.get('pass','api_key')