from tnote.config import data_dir
from pathlib import Path
import os


for file in os.listdir(data_dir):
    remove_file = Path(data_dir) / file
    os.remove(remove_file)
