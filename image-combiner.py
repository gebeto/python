from PIL import Image
import sys


def ignore_map(arr, key):
	result = []
	for item in arr:
		try:
			res = key(item)
			result.append(res)
		except:
			pass
	return result

def combine_images(images_paths):
	# images = [Image.open(image_path) for image_path in images_paths]
	images = ignore_map(images_paths, key = lambda image_path: Image.open(image_path))

	w = max([img.size[0] for img in images], default=0)
	h = sum([img.size[1] for img in images])

	result_img = Image.new('RGB', (w, h))

	for index, image in enumerate(images):
		result_img.paste(
			image,
			(
				0,
				sum([image.size[1] for image in images[:index]])
			)
		)

	return result_img



img = combine_images(sys.argv[1:])
img.save("out.jpg")
