#################
#page generation functions:
#################
import forget

def genNavBar(content_obj,total_pages,forFolder):
	if forFolder:
		index = content_obj.iFolderNumber
	else:
		index = content_obj.iSiteNumber
	prev = index - 1
	if prev < 1: prev = 1
	nextp = index + 1
	if nextp > total_pages: nextp = total_pages
	navbar_dict = {'next': nextp, 'prev': prev}
	navbar_str = forget.form('navbar.html',navbar_dict)
	return navbar_str
def genNavBarSite(content_obj,total_pages):
	return genNavBar(content_obj,total_pages,False)
def genNavBarFolder(content_obj,total_pages):
	return genNavBar(content_obj,total_pages,True)

def genPage(content_obj,folder_obj,forFolder):
	forget_dict = {'content_str':content_obj.get_content_str(folder_obj),'title_img':folder_obj.sTitleImg,'NavBar':genNavBar(content_obj,folder_obj.iFolderTotal,forFolder),}
	page_str = forget.form('template.html',forget_dict)
	return page_str
def genSitePage(content_obj,folder_obj):
	return genPage(content_obj,folder_obj,False)
def genFolderPage(content_obj,folder_obj):
	return genPage(content_obj,folder_obj,True)

def genRandomPage(total_pages):
	forget_dict = {'rand_max': total_pages}
	page_str = forget.form('random.html',forget_dict)
	return page_str

def genArchiveLink(date,title,number):
	forget_dict = {'date': date, 'title': title, 'number': number}
	link_str = forget.form('archive_link.html',forget_dict)
	return link_str

def genArchivePage(link_list_str,sTitleImg):
	forget_dict = {'link_list': link_list_str, 'title_img': sTitleImg}
	page_str = forget.form('archive.html',forget_dict)
	return page_str


import time
from email import utils
def genItemRSS(content_obj):
	forget_dict = {}
	forget_dict['url'] = str(content_obj.iSiteNumber) + '.html'
	forget_dict['title'] = content_obj.sTitle
	t = time.strptime(content_obj.dtCreated,'%Y-%m-%d %H:%M:%S')
	nowtimestamp = time.mktime(t)
	forget_dict['date'] = utils.formatdate(nowtimestamp)
	desc = content_obj.sToolText
	if desc:
		forget_dict['desc'] = desc
	item_str = forget.form('item.rss',forget_dict)
	return item_str


def writePage(dest_path,page_str):
	with open(dest_path,'w') as outfile:
		outfile.write(page_str)
