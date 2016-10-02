import xbmc, xbmcgui
import json

from decoder.net import WebSocketDecoder
from decoder.media import RD45Decoder
from decoder.bsi import BSIDecoder

from lib.overlays.volume import VolumeOverlay
from lib.overlays.rpm import RPMOverlay
from lib.core import get_current_window_id, throttle, run_async

DECODERS = [
    'decoder.bsi.BSIDecoder',
    'decoder.media.RD45Decoder',
]


class NavigationDecoder(WebSocketDecoder):

    def __init__(self):
        super(NavigationDecoder, self).__init__(
            DECODERS, proxy_attributes=True, parse_subscribed_only=True)
        # self.rd45 = RD45Decoder()
        # self.bsi = BSIDecoder()

        self.monitor = xbmc.Monitor()
        self.on('0x3e5', self.openMenu)
        self.on('0x165', self.changeRadioStatus)
        self.on('0x1a5', self.changeVolume)

        self.on('0x0b6', self.change_rpm)

        self.prev_window_id = 0
        self._source = None
        self._orign_volume = None
        self._volume_overlay = VolumeOverlay()

        self._rpm_overlay = RPMOverlay()
        self._rpm_overlay.show()
        self._rpm_overlay.rpm = 0

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

    @throttle(1)
    def changeVolume(self, *args):

        if self._orign_volume and self._orign_volume != self.volume:

            self._volume_overlay.show()
            self._volume_overlay.volume = self.volume
            xbmc.sleep(500)
            self._volume_overlay.hide()
        self._orign_volume = self.volume

    @throttle(1)
    def change_rpm(self, *args):

        # xbmcgui.Dialog().notification(json.dumps(self.bsi.rpm), '',
        #                               xbmcgui.NOTIFICATION_INFO, 200)
        # if (abs(self.bsi.rpm - self._rpm_overlay.rpm) > 200):
        self._rpm_overlay.rpm = self.bsi.rpm