#########
#GET DATA FUNCTIONS
#########
#dictionaries and lists get passed by 'reference', as they are mutable objects.
import data_classes
def getFolderData(sql_str,cur,folder_dict,title_folder_dict):
	"""passes back by reference a dictionary of folder objects and the title_folder_dict"""
	cur.execute(sql_str)
	rows = cur.fetchall()
	column_names = next(zip(*cur.description))
	for row in rows:
		folder_obj = data_classes.folder_data()
		for i,column_name in enumerate(column_names):
			exec('folder_obj.' + column_name + ' = row[i]')
		folder_dict[folder_obj.sFolder] = folder_obj
		title_folder_dict[folder_obj.sFolder] = []

def content_list_gen(rows,column_names):
	"""generator for content_objs"""
	for row in rows:
		content_obj = data_classes.content_data()
		for i,column_name in enumerate(column_names):
			exec('content_obj.' + column_name + ' = row[i]')
		yield content_obj

def getContentData(sql_str,cur):
	"""returns list of content objects"""
	cur.execute(sql_str)
	rows = cur.fetchall()
	column_names = next(zip(*cur.description))
	content_list = content_list_gen(rows,column_names)
	return content_list

from data_classes import *
def getFolderObj(cur,folder_name):
	sql_str = "SELECT * FROM tblFolders WHERE sFolder = '" + folder_name + "';"
	cur.execute(sql_str)
	row = cur.fetchone()
	if row == None:
		print('No such folder; exiting')
		exit()
	column_names = next(zip(*cur.description))
	folder_obj = folder_data()
	for i,column_name in enumerate(column_names):
		exec('folder_obj.' + column_name + ' = row[i]')
	return folder_obj

def getSiteCount(cur):
	sql_str = 'SELECT COUNT(*) FROM tblContent;'
	cur.execute(sql_str)
	site_total = cur.fetchone()[0]
	return site_total

def getFolderCount(cur,folder_name):
	sql_str = "SELECT COUNT(*) FROM tblContent WHERE sFolder = '" + folder_name + "';"
	cur.execute(sql_str)
	folder_total = cur.fetchone()[0]
	return folder_total
