import sublime, sublime_plugin

class CapitalizeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		print(type(self.view.sel()))
		for reg in self.view.sel():
			selected_text = self.view.substr(reg)
			output = selected_text.capitalize()
			self.view.replace(edit, reg, output)
