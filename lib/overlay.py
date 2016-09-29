import xbmc, xbmcgui
import os
import xml.etree.ElementTree as ET

from lib.utils import get_current_window_id


def _get_skin_resolution():
    skin_path = xbmc.translatePath('special://skin/')
    tree = ET.parse(os.path.join(skin_path, 'addon.xml'))
    try:
        res = tree.findall('./extension/res')[0]
    except:
        res = tree.findall('./res')[0]

    return int(res.attrib['width']), int(res.attrib['height'])

VIEWPORT_WIDTH, VIEWPORT_HEIGHT = _get_skin_resolution()


class Overlay(object):

    def __init__(self):
        self._controls = []
        self.showing = False
        self.window = None
        self.window_id = None
        self.viewport_width = VIEWPORT_WIDTH
        self.viewport_height = VIEWPORT_HEIGHT



    def add_control(self, control):
        self._controls.append(control)

    def remove_control(self, control):
        self._controls.remove(control)

    def show(self):
        if not self.showing:
            self.showing = True
            self.window_id = get_current_window_id()
            self.window = xbmcgui.Window(self.window_id)
            self.window.addControls(self._controls)

    def hide(self):
        if self.showing:
            self.showing = False
            self.window.removeControls(self._controls)

