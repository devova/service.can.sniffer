import sys
import os
MODULE_PATH = os.path.dirname(__file__)
sys.path.append(MODULE_PATH)
sys.path.append(os.path.join(MODULE_PATH, 'eggs'))
sys.path.append('/Users/devova/PycharmProjects/citrocan/app')

if os.environ.get('PYTHON_DEBUG_HOST'):
    try:
        sys.path.append(os.path.join(MODULE_PATH, 'pycharmdebug'))
        from pycharmdebug import pydevd
        pydevd.settrace('localhost', port=5678, stdoutToServer=True, stderrToServer=True)
    except ImportError:
        pass

import xbmc
import xbmcgui
import decoder

from lib import utils, socket_server
# from decoder.telnet import TelnetDecoder

commport = 51456

if __name__ == '__main__':
    # decoder = TelnetDecoder(decoder.DEFAULT_DECODERS, proxy_attributes=True)
    # decoder.connect('127.0.0.1', 8333)
    socket_server.start()
    addon = utils.ADDON
    addonname = utils.ADDON_NAME

    host = 'localhost'


    # xbmcgui.Dialog().ok(addonname, 'Start', 'Start', 'Start')


    monitor = xbmc.Monitor()
 
    while not monitor.abortRequested():

        line2 = 'Test'

        xbmcgui.Dialog().notification(addonname, line2)
        # xmbc.setInfoLabel('Citroen.Test', addonname)
        # Sleep/wait for abort for 10 seconds
        if monitor.waitForAbort(10):
            # Abort was requested while waiting. We should exit
            break
