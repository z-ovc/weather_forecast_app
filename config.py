import configparser

config = configparser.ConfigParser()
config.read("config.txt")
my_api_key = config.get('pass','my_api_key')