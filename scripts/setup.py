import sqlite3
from pathlib import Path

#reference dir_path and cur statically.
class Setup:
	dir_path = Path(__file__).absolute().parent.parent	
	_db_file = dir_path / 'data' / 'site_data'
	
	conn = sqlite3.connect(_db_file)
	cur = conn.cursor()

	dest_folder = dir_path / 'site_pages'
	source_folder = dir_path / 'pregen_pages'
	source_templates = dir_path / 'forms'
