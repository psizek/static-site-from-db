#forget - FORm GEneration Tool

#-----
#FORMS
#-----

import re
class Form:
	"""
	contains members for setting forms
	members:
	init_str - this is the unparsed string.
	t_str - this is the parsed string.
	form_dict - this defines which form substitutions to make.
	"""

	def __init__(self,init_str,form_dict={}):
		"""
		:param init_str: initial unparsed string
		:param form_dict={}: dictionary defining which substitutions to make
		"""
		self.delim1 = '[['
		self.delim2 = ']]'
		self.delim_mid = '##'
		self.init_str = init_str
		self.form_dict = form_dict

	def add(self,key,value):
		"""adds key value pair to form_dict"""
		self.form_dict[key] = value
	def delete(self,key):
		"""removes key value pair from form_dict"""
		del self.form_dict[key]

	def form_eval(self):
		""" given a string and args, attempts to perform regex replacem"ents to fill in the form. Matches on <delim1><tag><delim_mid><default><delim2>. Right now, these can only span a single line. """

		prev_t_str = ""
		self.t_str = self.init_str
		while prev_t_str != self.t_str: #run in case more tags pop up.
			prev_t_str = self.t_str
			for tag in self.form_dict:
				r_str = str(self.form_dict[tag])
				pattern = re.escape(self.delim1) + tag + re.escape(self.delim_mid) + '((.|' + re.escape('\n') + ')*?)' + re.escape(self.delim2)
				self.t_str = re.sub(pattern,r_str,self.t_str)

		#cleanup missing tags.
		pattern = re.escape(self.delim1) + '.+?' + re.escape(self.delim_mid) + '((.|' + re.escape('\n') + ')*?)' + re.escape(self.delim2)
		self.t_str = re.sub(pattern,'\\1',self.t_str)

		return self.t_str


#---------
#file operations

from pathlib import Path
def form(form_file,form_dict):
	"""
	generates a return string from form function.

	:param form_file: file which we use for replacements
	:param form_dict: how to perform form replacements.
	"""

	root_path = Path(__file__).absolute().parent.parent
	form_file = root_path / 'forms' / form_file
	with open(form_file,'r') as fin:
		f = Form(fin.read(),form_dict)
	return f.form_eval()

def form_x(form_file,*args):
	"""
	same as above, except assumes all tags in the form are number, and uses the additional arguments in *args to fill out those tag values.

	:param form_file: file which we use for replacements
	:param *args: optional optional arguments which contain the form entries for the file in question, by number.
	"""
	form_dict = {}
	count = 0
	for arg in args:
		count += 1
		form_dict[str(count)] = str(arg)
	return form(form_file,form_dict)
