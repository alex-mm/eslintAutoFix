import sublime, sublime_plugin

SETTINGS_KEY = 'ESLintAutoFix.sublime-settings'
DEFAULT_ESLINT_PATH = ''
DEFAULT_SHOW_PANEL = True

class Preferences:
  def load(self, settings):
    self.eslint_path = settings.get('eslint_path', DEFAULT_ESLINT_PATH)
    self.show_panel = settings.get('show_panel', DEFAULT_SHOW_PANEL)

Pref = Preferences()

def plugin_loaded():
  settings = sublime.load_settings(SETTINGS_KEY)
  Pref.load(settings)
  settings.add_on_change('reload', lambda: Pref.load(settings))

class Eslint_auto_fixCommand(sublime_plugin.WindowCommand):
	def run(self):
		fileName = self.window.active_view().file_name();
		args = {
		  'cmd': [
		    'eslint',
		    '--fix',
		    '--no-ignore',
		    fileName
		  ],
		  'path': Pref.eslint_path
		}
		self.window.run_command('exec', args)
		if not Pref.show_panel:
		  self.window.run_command("hide_panel", {"panel": "output.exec"})
	


