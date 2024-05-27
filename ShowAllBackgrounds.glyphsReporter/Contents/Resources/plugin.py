# encoding: utf-8
from __future__ import division, print_function, unicode_literals

###########################################################################################################
#
#
# Reporter Plugin
#
# Read the docs:
# https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Reporter
#
#
###########################################################################################################

import objc
from GlyphsApp import Glyphs
from GlyphsApp.plugins import ReporterPlugin
from AppKit import NSColor, NSCommandKeyMask


class ShowAllBackgrounds(ReporterPlugin):
	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': u'All Backgrounds',
			'de': u'Alle Hintergründe',
			'es': u'todos los fondos',
			'fr': u'tous les arrière-plans',
		})
		self.keyboardShortcut = '^'
		self.keyboardShortcutModifier = NSCommandKeyMask
		# NSShiftKeyMask | NSControlKeyMask | NSCommandKeyMask | NSAlternateKeyMask

	@objc.python_method
	def inactiveLayerBackground(self, layer):
		NSColor.colorWithRed_green_blue_alpha_(.8, .1, .2, .3).set()
		if layer.background.bezierPath:
			layer.background.bezierPath.fill()
		NSColor.colorWithRed_green_blue_alpha_(.8, .4, .0, .3).set()
		for backgroundComponent in layer.background.components:
			backgroundComponent.bezierPath.fill()

	def needsExtraMainOutlineDrawingForInactiveLayer_(self, layer):
		return True

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
