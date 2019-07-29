from nowatermark import WatermarkRemover
from PIL import Image
import glob
import sys
import os

script, watermark, products = sys.argv

# watermark_template_file_path = os.path.join(os.path.dirname(__file__), 'watermark.jpg')
# watermark_template_file_path = os.path.join(os.path.dirname(__file__), watermark)
# watermark_template_file_path = os.path.join(os.getcwd(), watermark)
watermark_template_file_path = watermark
remover = WatermarkRemover()
remover.load_watermark_template(watermark_template_file_path)


def png_to_jpg(path):
	image = Image.open(path)
	new_image = Image.new("RGBA", image.size, "WHITE")
	new_path = path
	try:
		new_image.paste(image, (0, 0), image)
		new_image.convert('RGB').save(new_path, "JPEG")
	except: pass
	return new_path


def remove_products_watermark():
	images = glob.glob(os.path.join(products, "**/photos/*.jpg"))
	for image in images:
		try:
			image = png_to_jpg(image)
			print(image)
			remover.remove_watermark(image, image)
		except: pass


remove_products_watermark()