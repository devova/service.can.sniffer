import xbmc
from decoder.net import WebSocketDecoder

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
        self._source = None

    @property
    def terminate(self):
        return self.monitor.abortRequested()

    def openMenu(self, *args):
        if self.rkeys.get('menu'):
            xbmc.executebuiltin('ActivateWindow(home)')

    def changeRadioStatus(self, *args):
        if self._source != self.source:
            if self.source == 'Tuner':
                self._source = self.source
                xbmc.executebuiltin('RunAddon(script.rd45.radio)')
            # else:
            #     xbmc.executebuiltin('StopScript(script.rd45.radio)')

        self._source = self.source