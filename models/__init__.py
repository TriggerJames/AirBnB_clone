#!usr/bin/python3

from models.engine.file.storage import FileStorage

def reload_storage():
    
    """Reloads the storage data from the file."""
    
    storage = FileStorage()
    storage.reload()

reload_storage()