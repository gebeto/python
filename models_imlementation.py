class Field(object):
	_counter = 0

	def __init__(self, formatter = lambda x: x):
		self.counter = Field._counter
		self.formatter = formatter
		Field._counter += 1

	def process(self, d):
		return self.formatter(d)

class Integer(Field):
	pass

class String(Field):
	pass

class Real(Field):
	pass

class Boolean(Field):
	pass



class Model(object):
	@property
	def fields(self):
		items = vars(self.__class__).items()
		filtered_items = [(key, cls) for key, cls in items if isinstance(cls, Field)]
		sorted_items = sorted(filtered_items, key=lambda a: a[1])
		return sorted_items

	def process(self, d):
		fields = self.fields
		processed = {}
		for key, field in fields:
			if not key in d: continue
			processed[key] = field.process(d[key])
		return processed
	

class Test1(Model):
	CCC = Integer(formatter=lambda x: x.upper())
	BBB = Integer()
	AAA = String()

class Test2(Model):
	BBB = Integer()
	CCC = Integer()
	AAA = String()





a = Test1()
res = a.process({
	"AAA": "Hello",
	"CCC": "Hello",
	"BBB": "Hello",
})

print res