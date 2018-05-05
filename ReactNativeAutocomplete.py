# import sublime
# import sublime_plugin



# def check_is_react_native_import(view):
# 	cursor_pos = view.sel()[0].begin()
# 	scope = view.extract_scope(cursor_pos)
# 	react_native_import = view.find(r"from [\"']react-native[\"']", scope.end())
# 	return react_native_import.a > 0


# class ReactNativeAutocomplete(sublime_plugin.EventListener):
# 	def on_query_completions(self, view, prefix, locations):
# 		line_region = view.full_line(locations[0])
# 		line_text = view.substr(line_region).strip()

# 		is_react_native_imports = check_is_react_native_import(view)
# 		if is_react_native_imports:
# 			return [
# 				["View", "View"],
# 				["Text", "Text"],
# 				["OpacityHighlight", "OpacityHighlight"],
# 			]

# 		print(line_text)
# 		res = "<"
# 		res += line_text
# 		res += " ${1:P}${1/(P)|()|.*/(?1:\\/\>)$3(?2:\>\<\/"
# 		res += line_text
# 		res += "\>)/}"
# 		return [
# 			# [line_text, "<%s $1/>" % line_text]
# 			# [line_text, "getElement${1/(T)|.*/(?1:s)/}By${1:T}${1/(T)|(I)|.*/(?1:agName)(?2:d)/}('$2')"]
# 			# [line_text, "getElement${1/(P)|.*/(?1:s)/}By${1:P}${1/(P)|(C)|.*/(?1:\ \/\>)(?2:\>\<\/\>)/}('$2')"]
# 			# [line_text, "getElement${1:P}${1/(P)|(C)|.*/(?1:\ \/\>)(?2:\>\<\/\>)/}('$2')"]
# 			[line_text, res]
# 		]

# 		return False
