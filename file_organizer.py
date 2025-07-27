import os
import shutil

class FileOrganizer:
    def __init__(self, target_folder):
        self.target_folder = target_folder
        self.extension_mapping = {
            'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
            'Documents': ['.pdf', '.docx', '.doc', '.txt', '.xlsx'],
            'Videos': ['.mp4', '.mkv', '.mov', '.avi'],
            'Audio': ['.mp3', '.wav'],
            'Archives': ['.zip', '.rar', '.tar', '.gz'],
            'Scripts': ['.py', '.js', '.sh', '.html', '.css'],
            'Others': []
        }

    def create_folder(self, folder_name):
        folder_path = os.path.join(self.target_folder, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    def get_category(self, extension):
        for category, extensions in self.extension_mapping.items():
            if extension.lower() in extensions:
                return category
        return 'Others'

    def organize(self):
        for item in os.listdir(self.target_folder):
            item_path = os.path.join(self.target_folder, item)
            if os.path.isfile(item_path):
                ext = os.path.splitext(item)[1]
                category = self.get_category(ext)
                self.create_folder(category)
                dest_path = os.path.join(self.target_folder, category, item)
                shutil.move(item_path, dest_path)
        print("✅ Files Organized Successfully!")
