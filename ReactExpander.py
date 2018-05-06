import sublime
import sublime_plugin

import re


class ReactExpanderAutocomplete(sublime_plugin.EventListener):
	def on_query_completions(self, view, prefix, locations):
		sn = view.scope_name(locations[0])

		is_ok = False
		if "meta.block.tsx" in sn or "meta.block.jsx" in sn:
			is_ok = True
		if not is_ok:
			return None

		p = prefix.strip()

		return [
			[
				"{P}\t<{P}><{P}/>".format(P=p),
				"<%s>\n\t$1\n</%s>" % (p, p)
			],
			[
				"{P}\t<{P}/>".format(P=p),
				"<%s $1 />" % (p)
			],
		]
