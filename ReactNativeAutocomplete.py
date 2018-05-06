import sublime
import sublime_plugin

import re


autocompletes = {
	"Alert": [
		["Prompt", "Prompt(${1:title}, ${2:message})"],
		["Alert", "Alert(${1:title}, ${2:message})"],
		["Confirm", "Confirm(${1:title}, ${2:message})"],
	],
	"SMAlert": [
		["Prompt", "Prompt(${1:title}, ${2:message})"],
		["Alert", "Alert(${1:title}, ${2:message})"],
		["Confirm", "Confirm(${1:title}, ${2:message})"],
	],
}


class ReactNativeAutocomplete(sublime_plugin.EventListener):
	def on_query_completions(self, view, prefix, locations):
		sn = view.scope_name(locations[0])

		is_ok = False
		# if "meta.block.tsx" in sn or "meta.block.jsx" in sn:
		if "source.tsx" in sn or "source.jsx" in sn:
			is_ok = True
		if not is_ok:
			return None

		curr_pos = view.sel()[0].begin()
		current_obj_region = view.word(curr_pos - 1)
		current_obj = view.substr(current_obj_region)

		return autocompletes.get(current_obj)
