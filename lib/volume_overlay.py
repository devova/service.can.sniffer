import xbmcgui

from lib.overlay import Overlay


class VolumeOverlay(Overlay):

    def __init__(self, volume):
        super(VolumeOverlay, self).__init__()
        self._volume = 0
        viewport_w, viewport_h = self.viewport_width, self.viewport_height
        font = 'font35_title'
        window_w = int(float(viewport_w) / 4)
        window_h = int(float(viewport_h) / 5)
        x = int(float(viewport_w - window_w) / 2)
        y = int(float(viewport_h) * 3 / 4 - window_h / 2)

        # main window
        self._background = xbmcgui.ControlImage(
            x, y, window_w, window_h, 'ContentPanel.png')
        self.add_control(self._background)

        self._title = xbmcgui.ControlLabel(
            x, y + 10, window_w, 40, '',
            font=font, textColor='0xFFFFFFFF', alignment=2)
        self.add_control(self._title)

        self._progress = xbmcgui.ControlProgress(
            x + 20, y + 80, window_w - 20, 20)
        self.add_control(self._progress)

        self.volume = volume

    @property
    def volume(self):
        return self._volume

    @volume.setter
    def volume(self, volume):
        self._volume = volume
        self._title.setLabel('VOLUME %s' % volume)
        self._progress.setPercent(volume * 100 / 25)

