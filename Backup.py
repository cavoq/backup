import os 
import yaml

class Backup:
	def __init__(self):
		self.get_input_directories()
		self.copy_directories()


	def get_input_directories(self):
		with open("Config.yml", "r") as file:
			self.data = yaml.load(file, Loader=yaml.FullLoader)
			self.Backup_directory = self.data["Backup-Directory"][0]

	def copy_directories(self):
		for directory in self.data["Directories"]:
			try: 
				os.system("sudo cp -r " + directory + " " +  self.Backup_directory)
			except:
				print("Check if your Config file is set correctly")
				break

B = Backup()