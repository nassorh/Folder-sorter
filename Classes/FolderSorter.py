from Database.database import db
import os
from Classes.File import File 

class Folder_Sorter():
    @classmethod
    def get_all_files(cls,directory) -> list:
        files = []
        if os.path.isdir(directory):
            all_files = os.listdir(directory)
            for file in all_files:
                temp_file_object = File()
                temp_file_object.name = file 
                temp_file_object.path = directory+"/"+file
                temp_file_object.extension = cls.get_extension(file)
                temp_file_object.catergory = cls.get_catergory(temp_file_object.extension)
                files.append(temp_file_object)
            return files
        else:
            raise Exception("File Directory is not valid")

    @staticmethod
    def get_extension(file_name: str) -> str:
        if "." in file_name:
            extension = file_name.split(".")
            extension = extension[-1].lower()
            return extension
        return None

    @staticmethod
    def get_catergory(extension: str) -> str:
        extensions_catergory = db.get_extensions()
        for row in extensions_catergory:
            if extension == row[0]:
                return row[1]
         
        return None
    
    @classmethod
    def move_files(cls,current_dir: str,files: list):
        files = files
        for file in files:
            if file.catergory:
                source_directory = file.path
                destination_directory = current_dir + "/" + file.catergory 
                destination_file_directory = destination_directory + "/" + file.name

                try:
                    os.rename(source_directory,destination_file_directory)
                except FileNotFoundError:
                    cls.create_folder(destination_directory)
                    os.rename(source_directory,destination_file_directory)
    
    @staticmethod
    def create_folder(file_directory: str):
        try:
            os.mkdir(file_directory)
        except FileExistsError:
            pass  
