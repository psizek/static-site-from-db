import datetime

#need to have functions that:
#1) ask for inputs and set data accordingly
#2) ask for a json dict and sets data accordingly
#3) constructs the content string
#4) exports to json
#so we're going to break 1 and 2 up into two different functions, and have a 'set data' function that relies on a dictionary as input.

#we're not going to save image data in the db, although it might be a good idea to do that later. Also should create a seperate git repository for site pages.
class content_data:
	iSiteNumber = 0
	iFolderNumber = 0
	sFolder = ''
	dtCreated = ''
	sContentClass = ''
	sContentOverride = ''
	sTitle = ''
	sToolText = ''
	sImgFile = ''

	manual_override = '' #work on this later, if needed.

	content_str = ''

	def get_content_str(self,folder_obj):
		"""gets content string. Creates content string if it doesn't already exist"""
		if self.content_str == '':
			return self.create_content_str(folder_obj)
		else: return self.content_str

	def create_content_str(self,folder_obj):
		"""constructs and returns the content_str. DOES NOT SET DATA, except for self.content_str"""
		if self.sContentClass == '':
			con_class = folder_obj.sDefContentClass
		else:
			con_class = self.sContentClass

		if self.sContentOverride != None:
			self.content_str = self.sContentOverride
		else:
			self.content_str = '<a href="index.html"><img class="' + con_class + '" src="../img/' + self.sFolder + '/' + self.sImgFile + '" alt="Comic Image"></a>'
		#add stuff for content and tool_text if we ever want this to show up.
		return self.content_str

	def construct_from_dict(self,json_dict = ''):
		"""sets site data based on dict. Will fail if appropriate data isn't set."""
		if json_dict == '':
			exit()
		if json_dict['sSiteNumber'] == 0 or json_dict['sFolder'] == '' or json_dict['iFolderNumber'] == '':
			exit()

		self.sFolder = json_dict['sFolder']
		self.iFolderNumber = json_dict['iFolderNumber']
		self.iSiteNumber = json_dict['sSiteNumber']
		self.sContentClass = json_dict['sContentClass']

		if json_dict['sImgFile'] == '':
			self.sImgFile = str(self.iFolderNumber) + '.png'
		else:
			self.sImgFile = json_dict['sImgFile']

		self.sTitle = json_dict['sTitle']
		self.sToolText = json_dict['sToolText']
		self.sContentOverride = json_dict['sContentOverride']
		self.dtCreated = json_dict['dtCreated']

	def export_to_dict(self):
		json_dict = {
		'sFolder' : self.sFolder,
		'iFolderNumber' : self.iFolderNumber,
		'sSiteNumber' : self.iSiteNumber,
		'sImgFile' : self.sImgFile,
		'sContentClass' : self.sContentClass,
		'sTitle' : self.sTitle,
		'sToolText' : self.sToolText,
		'sContentOverride' : self.sContentOverride,
		'dtCreated' : self.dtCreated
		}
		return json_dict

class folder_data:
	sFolder = ''
	sDefContentClass = ''
	sTitleImg = ''
	iFolderTotal = 0

	def load_folder_dict(self,my_dict):
		self.sFolder = my_dict['sFolder']
		self.sTitleImg = my_dict['sTitleImg']
		self.sDefContentClass = my_dict['sDefContentClass']
		self.iFolderTotal = my_dict['iFolderTotal']

	def save_to_dict(self):
		ex_dict = {
			'sFolder' : self.sFolder,
			'sTitleImg' : self.sTitleImg,
			'sDefContentClass' : self.sDefContentClass,
			'iFolderTotal' : self.iFolderTotal
			}
		return ex_dict
