class Package(object):
	def __init__(self, package_info):
		super(Package, self).__init__()
		self.package = self.lines_to_dict(package_info) if type(package_info) == str else package_info
		self.name = self.package["Name"]

	def lines_to_dict(self, lines):
		lines = lines.split('\n')
		package_dict = {}
		for line in lines:
			package_dict[line.split(':')[0]] = ':'.join(line.split(':')[1:]).strip()
		return package_dict

	def __str__(self):
		return '\n'.join(["%s: %s" % (key, val) for key, val in self.package.items()]) + "\n\n"


