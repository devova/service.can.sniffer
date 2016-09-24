import sys
import os

MODULE_PATH = os.path.dirname(__file__)
sys.path.append(MODULE_PATH)
sys.path.append(os.path.join(MODULE_PATH, 'eggs'))
sys.path.append('/Users/devova/PycharmProjects/citrocan/app')

if False or os.environ.get('PYTHON_DEBUG_HOST'):
    try:
        sys.path.append(os.path.join(MODULE_PATH, 'pycharmdebug'))
        from pycharmdebug import pydevd
        pydevd.settrace('localhost', port=5678, stdoutToServer=True, stderrToServer=True)
    except ImportError:
        pass

import xbmc, xbmcgui
from lib.navigation_decoder import NavigationDecoder


if __name__ == '__main__':

    # xbmcgui.Dialog().ok('Yoo', 'Start', 'Start', 'Start')
    # monitor = xbmc.Monitor()
    # xbmc.executebuiltin('RunAddon(script.rd45.radio)')
    # for i in range(10):
    #     radio_active = xbmc.getCondVisibility('Window.IsActive(1100)')
    #     if not radio_active:
    #         xbmc.executebuiltin('RunAddon(script.rd45.radio)')
    #         monitor.waitForAbort(3)
    #     xbmc.executebuiltin('ActivateWindow(home)')
    #     monitor.waitForAbort(3)


    # while not monitor.abortRequested():

    decoder = NavigationDecoder()
    decoder.connect('ws://127.0.0.1:8593')
        # if monitor.waitForAbort(10):
        #     Abort was requested while waiting. We should exit
            # break
