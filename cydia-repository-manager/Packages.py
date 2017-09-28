from bz2 import BZ2File
from Package import Package


class Packages(object):
	def __init__(self, filename):
		super(Packages, self).__init__()
		self.filename = filename
		self.packages = {}
		self.loadPackages()

	def loadPackages(self):
		try: 
			file = BZ2File(self.filename)
		except:
			file = BZ2File(self.filename, "wb")
		raw_packages = [package for package in file.read().replace('\r', '').split('\n\n') if package != '']
		for package in raw_packages:
			# self.packages.append(Package(package))
			pkg = Package(package)
			self.packages[pkg.name] = pkg

	def addPackage(self, package):
		self.packages.append(Package({
				"Package": "net.winneonsword.package",
				"Version": "1.0",
				"Architecture": "iphoneos-arm",
				"Maintainer": "Jesse Bryan <winneonsword@gmail.com>",
				"Filename": "./Package.deb",
				"Size": "736",
				"Section": "Themes",
				"Homepage": "http://repo.winneonsword.net",
				"Description": "This is a test package from /u/WinneonSword's tutorial repository!",
				"Author": "Jesse Bryan <winneonsword@gmail.com>",
				"Depiction": "http://repo.winneonsword.net/packages/package.html",
				"Name": "Test Package"
			}))

	def savePackages(self):
		file = BZ2File(self.filename, "wb")
		for package in self.packages:
			file.write(str(package))

	def names(self):
		return self.packages.keys()

	def __str__(self):
		return "[" + ', '.join([str(type(pkg)) for pkg in self.packages.values()]) + "]"

	def __getitem__(self, i):
		if type(i) == int:
			return self.packages.values()[i]
		elif type(i) == str:
			return self.packages[i]

	def __len__(self):
		return len(self.packages)


# a = Packages('./repo/Packages.bz2')

# print a['Copic']
