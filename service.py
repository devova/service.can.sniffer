import sys
import os
MODULE_PATH = os.path.dirname(__file__)
sys.path.append(MODULE_PATH)
sys.path.append(os.path.join(MODULE_PATH, 'pycharmdebug'))

if os.environ.get('PYTHON_DEBUG_HOST'):
    try:
        from pycharmdebug import pydevd
        pydevd.settrace('localhost', port=5678, stdoutToServer=True, stderrToServer=True)
    except ImportError:
        pass

import xbmc
import xbmcaddon
import xbmcgui

if __name__ == '__main__':
    monitor = xbmc.Monitor()
 
    while not monitor.abortRequested():
        addon = xbmcaddon.Addon()
        addonname = addon.getAddonInfo('name')

        line2 = 'Test'

        xbmcgui.Dialog().notification(addonname, line2)

        # Sleep/wait for abort for 10 seconds
        if monitor.waitForAbort(10):
            # Abort was requested while waiting. We should exit
            break
