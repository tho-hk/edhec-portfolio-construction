'''
    Helper module for easy import of custom modules in Kaggle
    or any other 3rd platform outside GitHub
'''

import sys
import os
from pathlib import Path

class ModuleSetup:
    def __init__(self):
        self.added_paths = []
        # use current working directory as base (which is the cloned repo in Kaggle)
        self.base_path = Path.cwd()

    def add_directory(self, dir_name):
        """add a specific directory to Python path"""
        dir_path = self.base_path / dir_name
        if dir_path.exists():
            full_path = str(dir_path.absolute())
            if full_path not in sys.path:
                sys.path.insert(0, full_path)
                self.added_paths.append(dir_name)
                return True
        
        return False
    
    def auto_add_all(self):
        """Automatically add all directories with Python files"""
        added = []

        for item in self.base_path.iterdir():
            if (item.is_dir() and
                not item.name.startswith('.') and
                not item.name.startswith('__') and
                list(item.glob('*(.py)'))):

                if self.add_directory(item.name):
                    added.append(item.name)
        return added
    
    def show_status(self):
        """Show what directories were added"""
        print(f"Working from: {self.base_path}")
        if self.added_paths:
            print ("Added to Python path:")
            for path in self.added_paths:
                print(f"{path}/")
        else:
            print("No custom directories added")

# Global instance
module_setup = ModuleSetup()