
def to_upper_case(text):
	return text.upper()


def main(**kwargs):
	return to_upper_case(kwargs.get("text", "*ALTERNATE*"))