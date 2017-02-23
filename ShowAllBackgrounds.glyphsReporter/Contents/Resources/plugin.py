# encoding: utf-8

###########################################################################################################
#
#
#	Reporter Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Reporter
#
#
###########################################################################################################


from GlyphsApp.plugins import *

class ShowAllBackgrounds(ReporterPlugin):

	def settings(self):
		self.menuName = Glyphs.localize({'en': u'All Backgrounds', 'de': u'alle Hintergründe'})
		self.keyboardShortcut = '^'
		self.keyboardShortcutModifier = NSCommandKeyMask
		# NSShiftKeyMask | NSControlKeyMask | NSCommandKeyMask | NSAlternateKeyMask

	def inactiveLayers(self, layer):
		NSColor.colorWithRed_green_blue_alpha_(.8, .1, .2, .3).set()
		if layer.background.bezierPath:
			layer.background.bezierPath.fill()
		NSColor.colorWithRed_green_blue_alpha_(.8, .4, .0, .3).set()
		for backgroundComponent in layer.background.components:
			backgroundComponent.bezierPath.fill()

	def needsExtraMainOutlineDrawingForInactiveLayer_(self, layer):
		return True

