import data_classes
import sqlite3

#get inputs
#should have option to make this into tkinter later. As in seperate functions that parse into a result?
folder_name = input("Folder: ") #only one folder per page
if folder_name == '':
	exit()
titleInput = input('Title: ')
if titleInput == '':
	print('need title for archive page/rss! exiting')
	exit()
contentClassInput = input('Content Class (leave blank to default): ')
toolTextInput = input('Tool Text (optional): ')

#setup
from setup import Setup
conn = Setup.conn
cur = Setup.cur
dir_path = Setup.dir_path

#GET DATA
from get_data_fns import *
print("running retrieval")
folder_obj = getFolderObj(cur,folder_name)
site_total = getSiteCount(cur)
folder_total = getFolderCount(cur,folder_name)

#build object
def makeContentObj(titleInput,contentClassInput = '', toolTextInput = ''):
	import datetime
	now = datetime.datetime.now()
	content_obj = content_data()
	content_obj.sFolder = folder_name
	content_obj.dtCreated = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	content_obj.iSiteNumber = site_total + 1
	content_obj.iFolderNumber = folder_total + 1
	content_obj.sContentClass = contentClassInput
	if content_obj.sContentClass == '':
		content_obj.sContentClass = folder_obj.sDefContentClass
	content_obj.sImgFile = str(folder_total + 1) + '.png'
	content_obj.sToolText = toolTextInput
	content_obj.sTitle = titleInput
	#content override must be set manually
	return content_obj

content_obj = makeContentObj(titleInput,contentClassInput, toolTextInput)


#note that image must be named 'target.png'
def mvImgFile(dir_path,folder_name,content_obj):
	import os
	dest_path = dir_path + '/pregen_content/img/' + folder_name + '/' + content_obj.sImgFile
	source_path = dir_path + '/content_staging/target.png'
	os.rename(source_path, dest_path)

mvImgFile(dir_path,folder_name,content_obj)

################
#update database
############
from pprint import pprint
print('running updates')
try:
	#add content row
	val_list = (content_obj.sFolder,content_obj.dtCreated,content_obj.iSiteNumber,content_obj.iFolderNumber,content_obj.sContentClass,content_obj.sToolText,content_obj.sTitle,content_obj.sImgFile)
	sql_str = "INSERT INTO tblContent (sFolder, dtCreated, iSiteNumber, iFolderNumber, sContentClass, sToolText, sTitle, sImgFile) VALUES (?,?,?,?,?,?,?,?);"
	cur.execute(sql_str,val_list)

	#update counts
	sql_str = "UPDATE tblFolders SET iFolderTotal = ? WHERE sFolder = ?;"
	update_list = []
	val_list = (folder_total + 1, folder_name)
	update_list.append(val_list)
	val_list = (site_total + 1, 'all')
	update_list.append(val_list)
	cur.executemany(sql_str, update_list)
	conn.commit()
except sqlite3.Error as e:
	print ("Update error occurred: ", e.args[0])
