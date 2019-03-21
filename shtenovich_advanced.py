keyboard = [
	'a', 'b', 'c', 'd', 'e', 'f', 'g', '1', '2', '3', 'shift',
	'h', 'i', 'j', 'k', 'l', 'm', 'n', '4', '5', '6', ' ',
	'o', 'p', 'q', 'r', 's', 't', 'u', '7', '8', '9', 'backspace',
	'v', 'w', 'x', 'y', 'z', '-', '_', '@', '.', '0', 'enter'
]

columns = 11

def get_key_position(letter):
	index = keyboard.index(letter)
	return [int(index / columns), index % columns]

def moves(count, a, b):
	return [a if count > 0 else b for i in range(0, abs(count) + 1) if i is not 0]

def move_to_key(current_pos, key_pos):
	result = []
	# print(current_pos, key_pos, end=' ')
	y_moves_count = key_pos[0] - current_pos[0]
	x_moves_count = key_pos[1] - current_pos[1]
	# print([y_moves_count, x_moves_count], end=' ')
	y_moves = moves(y_moves_count, 'down', 'up')
	x_moves = moves(x_moves_count, 'right', 'left')
	# print([y_moves, x_moves])
	result += y_moves
	result += x_moves
	result += ['select']
	return key_pos, result

def steps_for(word):
	current_pos = [0, 0]
	result = []
	for letter in word:
		if letter.isupper():
			current_pos, steps = move_to_key(current_pos, get_key_position('shift'))
			result += steps
		letter = letter.lower()
		current_pos, steps = move_to_key(current_pos, get_key_position(letter))
		result += steps
	return result

print(steps_for("hint1"))