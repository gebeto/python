from Column import *


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


	def save(self, path = None):
		file_path = path if path else "{}.xlsx".format(self.title)
		self.wb.save(file_path)


	def _init_columns(self):
		wb = self.wb
		ws = self.ws

		for column_index, column in enumerate(self.columns):
			self.columns_dict[column.col_name] = column
			column.init(ws, column_index + 1)

		self._initialized = True
		return wb, ws
	


class Test1(Model):
	CCC = Integer('name', 'Name', formatter=lambda x: x.upper())
	BBB = Integer('sname', 'SecondName')
	AAA = Varchar('share', 'SirWhore')


# a = Test1()
# a.add_row({
# 	"AAA": "Hello",
# 	"CCC": "Hello",
# 	"BBB": "Hello",
# })

# a.add_row({
# 	"AAA": "Ama",
# 	"CCC": "Ama",
# 	"BBB": "Ama",
# })