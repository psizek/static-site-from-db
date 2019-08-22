#get data
#generate pages with strings and save to file

#setup
import data_classes
import forget
from pathlib import Path

import shutil

from setup import Setup
cur = Setup.cur
dest_folder = Setup.dest_folder

from get_data_fns import *
from page_gen_fns import *

#GET DATA
folder_dict = {}
title_folder_dict = {}
getFolderData('SELECT * FROM tblFolders',cur,folder_dict,title_folder_dict)

site_obj = folder_dict['all']

content_list = getContentData('SELECT * FROM tblContent',cur)

############
#generate page functions
############

def writeFolderPages(dest_folder,content_obj,folder_dict):
	folder_obj = folder_dict[content_obj.sFolder]
	page_str = genFolderPage(content_obj,folder_obj)
	folder_path = dest_folder / content_obj.sFolder
	filename = str(content_obj.iFolderNumber) + '.html'
	writePage(folder_path, filename, page_str)

def writeSitePages(dest_folder,content_obj,site_obj):
	page_str = genSitePage(content_obj,site_obj)
	folder_path = dest_folder / 'all'
	filename = str(content_obj.iSiteNumber) + '.html'
	writePage(folder_path, filename, page_str)

def writeIndexPages(dest_folder,folder_obj):
	cp_page = str(dest_folder) + '/' + folder_obj.sFolder + '/' + str(folder_obj.iFolderTotal) + '.html'
	dest_page = str(dest_folder) + '/' + folder_obj.sFolder + '/index.html'
	shutil.copyfile(cp_page, dest_page)

def writeRandomPages(dest_folder,folder_obj):
	page_str = genRandomPage(folder_obj.iFolderTotal)
	folder_path = dest_folder / folder_obj.sFolder
	filename = 'random.html'
	writePage(folder_path, filename, page_str)

def writeArchivePages(dest_folder,folder_obj,title_tup_list):
	link_list_str = ''
	for title_tup in title_tup_list:
		link_list_str += genArchiveLink(title_tup[0],title_tup[1],title_tup[2])
		link_list_str += '\n'
	page_str = genArchivePage(link_list_str,folder_obj.sTitleImg)
	folder_path = dest_folder / folder_obj.sFolder
	filename = 'archive.html'
	writePage(folder_path, filename, page_str)

#generate pages
for content_obj in content_list:

	writeFolderPages(dest_folder,content_obj,folder_dict)
	writeSitePages(dest_folder,content_obj,site_obj)

	#add to list of site links with title data
	title_tup = (content_obj.dtCreated,content_obj.sTitle,content_obj.iFolderNumber)
	title_folder_dict[content_obj.sFolder].append(title_tup)
	title_tup = (content_obj.dtCreated,content_obj.sTitle,content_obj.iSiteNumber)
	title_folder_dict['all'].append(title_tup)


for folder_str in folder_dict:
	folder_obj = folder_dict[folder_str]

	writeIndexPages(dest_folder,folder_obj)
	writeRandomPages(dest_folder,folder_obj)
	writeArchivePages(dest_folder,folder_obj,title_folder_dict[folder_str])
