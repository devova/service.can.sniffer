import os

import xbmcgui
from lib.overlay import Overlay
from lib.utils import ADDON_PATH


class RPMOverlay(Overlay):

    def __init__(self):
        super(RPMOverlay, self).__init__()
        viewport_w, viewport_h = self.viewport_width, self.viewport_height
        self._rpm = 0
        font = 'font35_title'
        window_w = 300
        window_h = 300
        x = int(float(viewport_w) / 4 - window_w / 2)
        y = int(float(viewport_h) / 4 - window_h / 2)

        self._rpm_gauge = xbmcgui.ControlImage(
            x, y, window_w, window_h,
            os.path.join(ADDON_PATH, 'resources', 'media', 'rpm.png'))
        self.add_control(self._rpm_gauge)

        self._rpm_arrow = xbmcgui.ControlImage(
            x, y, window_w, window_h,
            os.path.join(ADDON_PATH, 'resources', 'media', 'gauge-arrow.png'))
        self.add_control(self._rpm_arrow)

    def show(self):
        super(RPMOverlay, self).show()
        if self.showing:
            self._rpm_arrow.setAnimations(
                [('Conditional',
                  'effect=rotate end=-%s center=auto time=0 loop=false '
                  'reversible=false condition=true' % self.rpm_angle(0))])

    @property
    def rpm(self):
        return self._rpm

    @rpm.setter
    def rpm(self, rpm):
        self._rpm_arrow.setAnimations(
            [('Conditional',
              'effect=rotate end=-%s start=-%s center=auto time=500 loop=false '
              'reversible=false condition=true' % (
                  self.rpm_angle(rpm), self.rpm_angle(self._rpm)))])
        self._rpm = rpm

    def rpm_angle(self, rpm):
        return str(rpm * 260 / 8000 + 95)
