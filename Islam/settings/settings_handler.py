from configparser import ConfigParser
import os
from . import app
appName=app.appName
cpath=os.path.join(os.getenv('appdata'),appName,"settings.ini")
if not os.path.exists(os.path.join(os.getenv('appdata'),appName)):
	os.mkdir(os.path.join(os.getenv('appdata'),appName))
if not os.path.exists(cpath):
	config = ConfigParser() 
	config.add_section("g")
	config["g"]["lang"] = "en"
	config["g"]["exitDialog"] = "True"
	config.add_section("update")
	config["update"]["autoCheck"]="True"
	config["update"]["beta"]="False"
	config.add_section("prayerTimes")
	config["prayerTimes"]["country"]="EG"
	config["prayerTimes"]["city"]="cairo"
	config.add_section("sibha")
	config["sibha"]["run"]="True"
	config["sibha"]["duration"]="10"
	config["sibha"]["type"]="0"
	config.add_section("readQuran")
	config["readQuran"]["run"]="True"
	config["readQuran"]["duration"]="10"
	with open(cpath, "w",encoding="utf-8") as file:
		config.write(file)

def get(section,key):
	config = ConfigParser()
	config.read(cpath)
	value = config[section][key]
	return value


def set(section,key, value):
		config = ConfigParser()
		config.read(cpath)
		config[section][key] = value
		with open(cpath, "w",encoding="utf-8") as file:
			config.write(file)

