structure = [
	[0, "bLength", 1, "Размер дескриптора в байтах (всегда 18)"],
	[1, "bDescriptorType", 1, "Тип дескриптора (всегда 1)"],
	[2, "bcdUSB", 2, "Номер версии USB в формате BCD"],
	[4, "bDeviceClass", 1, "Код класса"],
	[5, "bDeviceSubClass", 1, "Код подкласса (всегда 0)"],
	[6, "bDeviceProtocol", 1, "Код протокола (всегда 0)"],
	[7, "bMaxPacketSize0", 1, "Максимальный размер пакета для нулевой конечной точки (64 для HS, 8 — для FS и LS)"],
	[8, "idVendor", 2, "Идентификатор производителя"],
	[10, "idProduct", 2, "Идентификатор продукта"],
	[12, "bcdDevice", 2, "Номер версии устройства в формате BCD"],
	[14, "iManufacturer", 1, "Индекс дескриптора строки, описывающей производителя"],
	[15, "iProduct", 1, "Индекс дескриптора строки, описывающей продукт"],
	# [16, "iSerialNumber", 1, "Индекс дескриптора строки, содержащей серийный номер устройства"],
	[16, "iSerial", 1, "Индекс дескриптора строки, содержащей серийный номер устройства"],
	[17, "bNumConfigurations", 1, "Количество возможных конфигураций устройства"],
]

import re
comp = re.compile(r"\s+")

def proc_line(line):
	stripped = line.strip()
	splitted = comp.split(stripped)
	return splitted[0], splitted[1]

logs = [proc_line(l) for l in open("iphone-xr.txt").readlines()]
logs_dict = {l[0]: l[1] for l in logs}
print(logs_dict)

for offset, name, size, description in structure:
	print(name, "=", logs_dict.get(name))