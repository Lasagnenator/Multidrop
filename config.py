import configparser
config = configparser.ConfigParser()

try:
    config.read("config.txt")
except:
    config.read("../config.txt")

name = config["user"]["name"]
UUID = config["user"]["uuid"]
