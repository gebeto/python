class Column(object):
	_counter = 0

	def __init__(self, key, col_name, formatter = lambda x: x, *args, **kwargs):
		self.counter = Column._counter
		self.formatter = formatter
		self.col_name = col_name
		self.key = key
		Column._counter += 1

	def process(self, d):
		return self.formatter(d)

class Integer(Column):
	def __init__(self, *args, **kwargs):
		super(Integer, self).__init__(*args, **kwargs)
		self.type = 'int'

class Varchar(Column):
	def __init__(self, *args, **kwargs):
		super(Varchar, self).__init__(*args, **kwargs)
		self.type = 'varchar'

class Real(Column):
	def __init__(self, *args, **kwargs):
		super(Real, self).__init__(*args, **kwargs)
		self.type = 'real'
		
class Boolean(Column):
	def __init__(self, *args, **kwargs):
		super(Boolean, self).__init__(*args, **kwargs)
		self.type = 'boolean'
		

class Model(object):
	@property
	def fields(self):
		items = vars(self.__class__).items()
		filtered_items = [(key, cls) for key, cls in items if isinstance(cls, Column)]
		sorted_items = sorted(filtered_items, key=lambda a: a[1])
		return sorted_items

	def _process(self, d):
		fields = self.fields
		processed = {}
		for key, field in fields:
			if not key in d: continue
			processed[field.key] = field.process(d[key])
		return processed

	def add_row(self, row):
		print self._process(row)
	

class Test1(Model):
	CCC = Integer('name', 'Name', formatter=lambda x: x.upper())
	BBB = Integer('sname', 'SecondName')
	AAA = Varchar('share', 'SirWhore')


a = Test1()
a.add_row({
	"AAA": "Hello",
	"CCC": "Hello",
	"BBB": "Hello",
})

a.add_row({
	"AAA": "Ama",
	"CCC": "Ama",
	"BBB": "Ama",
})