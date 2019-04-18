import forget

import datetime
import time
from email import utils

from setup import Setup

from get_data_fns import *
from page_gen_fns import *

cur = Setup.cur
dir_path = Setup.dir_path
dest_folder = Setup.dest_folder

folder_dict = {}
getFolderData('SELECT * FROM tblFolders',cur,folder_dict, {})

sql_str = 'SELECT * FROM tblContent ORDER BY iSiteNumber DESC LIMIT 5'
content_list = getContentData(sql_str,cur)

item_str = ''
for content_obj in content_list:
	item_str += genItemRSS(content_obj) + '\n'

rss_page = forget.form('WLT.rss',{'item_list': item_str})
dest_path = dest_folder + '/WLT.rss'
writePage(dest_path,rss_page)
