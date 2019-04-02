class PricelistColumn(object):
	def __init__(self, col_fill, col_name, col_type, col_title, col_color='FFFFFF', width=10):
		self.col_fill = col_fill
		self.col_name = col_name
		self.col_type = col_type
		self.col_title = col_title
		self.col_color = col_color

		self.cell_prototype = None
		self.col_index = None
		self.width = calculate_column_width(col_type)
		self.max_width = 0

	def init(self, ws, index):
		self.col_index = index
		current_fill = PatternFill("solid", fgColor=self.col_fill)

		cell1 = ws.cell(row=1, column=index)
		cell1.value = self.col_name
		cell1.fill = current_fill
		cell1.alignment = center_alignment
		# ws.row_dimensions[cell1.column_letter].height = long(100)
		ws.row_dimensions[1].height = 40
		ws.column_dimensions[cell1.column_letter].fill = current_fill

		self.cell_prototype = copy(cell1)
		ws.column_dimensions[cell1.column_letter].width = self.width

		cell2 = ws.cell(row=2, column=index, value=self.col_type)
		cell2.value = self.col_type
		cell2.fill = current_fill
		cell2.alignment = center_alignment
		ws.row_dimensions[2].height = 40

		cell3 = ws.cell(row=3, column=index, value=self.col_title)
		cell3.value = self.col_title
		cell3.fill = PatternFill("solid", fgColor="808080")
		cell3.font = Font(color="FFFFFF")
		cell3.alignment = center_alignment
		ws.row_dimensions[3].height = 60



class Column(object):
	__type__ = None
	__type_args__ = None
	_counter = 0

	@property
	def type(self):
		result = ""
		if self.__type__:
			result += self.__type__
		else:
			return ""
		if self.__type_args__:
			result += "({})".format(self.__type_args__)
		return result

	def __init__(self, key, formatter = lambda x: x, *args, **kwargs):
		self.counter = Column._counter
		Column._counter += 1
		self.formatter = formatter
		self.key = key

	def process(self, d):
		return self.formatter(d)

	def init(self, ws, index, col_name):
		self.col_index = index
		current_fill = PatternFill("solid", fgColor=self.col_fill)

		cell1 = ws.cell(row=1, column=index)
		cell1.value = self.col_name
		cell1.fill = current_fill
		cell1.alignment = center_alignment
		ws.row_dimensions[1].height = 40
		ws.column_dimensions[cell1.column_letter].fill = current_fill

		self.cell_prototype = copy(cell1)
		ws.column_dimensions[cell1.column_letter].width = self.width

		cell2 = ws.cell(row=2, column=index, value=self.col_type)
		cell2.value = self.col_type
		cell2.fill = current_fill
		cell2.alignment = center_alignment
		ws.row_dimensions[2].height = 40

		cell3 = ws.cell(row=3, column=index, value=self.col_title)
		cell3.value = self.col_title
		cell3.fill = PatternFill("solid", fgColor="808080")
		cell3.font = Font(color="FFFFFF")
		cell3.alignment = center_alignment
		ws.row_dimensions[3].height = 60



class Integer(Column):
	__type__ = 'int'


class Varchar(Column):
	__type__ = 'varchar'
	def __init__(self, *args, **kwargs):
		super(Varchar, self).__init__(*args, **kwargs)
		length = kwargs.get('length', None)
		if length:
			self.__type_args__ = length


class Real(Column):
	__type__ = 'real'

		
class Boolean(Column):
	__type__ = 'boolean'



a = Varchar('kok', length="22")
print a.process('hello')
