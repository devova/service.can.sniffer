import xbmc
from decoder.net import WebSocketDecoder
from lib.volume_overlay import VolumeOverlay
from lib.utils import get_current_window_id

DECODERS = [
    'decoder.media.RD45Decoder',
    'decoder.bsi.BSIDecoder'
]


class NavigationDecoder(WebSocketDecoder):

    def __init__(self):
        super(NavigationDecoder, self).__init__(DECODERS, proxy_attributes=True)
        self.monitor = xbmc.Monitor()
        self.on('0x3e5', self.openMenu)
        self.on('0x165', self.changeRadioStatus)
        self.on('0x1a5', self.changeVolume)

        self._source = None
        self._orign_volume = None
        self._volume_overlay = VolumeOverlay(0)
        self.prev_window_id = 0

    @property
    def terminate(self):
        return self.monitor.abortRequested()

    def openMenu(self, *args):
        if self.rkeys.get('menu'):
            window_id = get_current_window_id()
            if window_id != 1000:
                self.prev_window_id = window_id
            xbmc.executebuiltin('ActivateWindow(home)')
        if self.rkeys.get('mode') and self.prev_window_id:
            xbmc.executebuiltin('ActivateWindow(' + self.prev_window_id + ')')

    def changeRadioStatus(self, *args):
        if self._source != self.source:
            if self.source == 'Tuner':
                self._source = self.source
                xbmc.executebuiltin('RunAddon(script.rd45.radio)')
            # else:
            #     xbmc.executebuiltin('StopScript(script.rd45.radio)')

        self._source = self.source

    def changeVolume(self, *args):

        if self._orign_volume and self._orign_volume != self.volume:
            # xbmcgui.Dialog().notification('VOLUME %s' % self.volume, '', xbmcgui.NOTIFICATION_INFO, 200)
            self._volume_overlay.show()
            self._volume_overlay.volume = self.volume
            xbmc.sleep(2000)
            self._volume_overlay.hide()

        self._orign_volume = self.volume