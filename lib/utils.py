import json

import xbmc
import xbmcaddon

ADDON = xbmcaddon.Addon()
ADDON_ID = ADDON.getAddonInfo('id').decode("utf-8")
ADDON_ICON = ADDON.getAddonInfo('icon').decode("utf-8")
ADDON_NAME = ADDON.getAddonInfo('name').decode("utf-8")
ADDON_PATH = ADDON.getAddonInfo('path').decode("utf-8")


def get_current_window_id():
    current_window = xbmc.executeJSONRPC(
        '{"jsonrpc":"2.0","id":1,"method":"GUI.GetProperties",'
        '"params":{"properties":["currentwindow"]}}')
    return json.loads(current_window)["result"]["currentwindow"]["id"]