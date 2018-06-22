from PIL import ImageDraw


class ImageDrawSlavik(ImageDraw.ImageDraw):
	"""docstring for ImageDrawSlavik"""
	def __init__(self, im, mode=None):
		super(ImageDrawSlavik, self).__init__(im, mode)


	def text(self, xy, text, fill=None, font=None, anchor=None, *args, **kwargs):
		if self._multiline_check(text):
			return self.multiline_text(xy, text, fill, font, anchor, *args, **kwargs)
		ink, fill = self._getink(fill)
		if font is None:
			font = self.getfont()
		if ink is None:
			ink = fill
		if ink is not None:
			try:
				mask, offset = font.getmask2(text, self.fontmode, *args, **kwargs)
				xy = xy[0] + offset[0], xy[1] + offset[1]
			except AttributeError:
				try:
					mask = font.getmask(text, self.fontmode, *args, **kwargs)
				except TypeError:
					mask = font.getmask(text)
			self.draw.draw_bitmap(xy, mask, ink)
		return xy


	def multiline_text(self, xy, text, fill=None, font=None, anchor=None,
					   spacing=4, align="left", direction=None, features=None):
		widths = []
		max_width = 0
		lines = self._multiline_split(text)
		line_spacing = self.textsize('A', font=font)[1] + spacing
		for line in lines:
			line_width, line_height = self.textsize(line, font)
			widths.append(line_width)
			max_width = max(max_width, line_width)
		left, top = xy
		for idx, line in enumerate(lines):
			if align == "left":
				pass  # left = x
			elif align == "center":
				left += (max_width - widths[idx]) / 2.0
			elif align == "right":
				left += (max_width - widths[idx])
			else:
				assert False, 'align must be "left", "center" or "right"'
			self.text((left, top), line, fill, font, anchor,
					  direction=direction, features=features)
			top += line_spacing
			left = xy[0]


	def text_box(self, xy, box, texts=[], font=None, spacing=4, **kwargs):
		fill = kwargs["fill"]
		hfill = kwargs["hfill"]
		for text in texts:
			print self.text(xy, text)
		