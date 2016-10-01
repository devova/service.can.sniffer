import json
from threading import Thread, Timer
from functools import wraps

import time

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


def debounce(wait):
    """ Decorator that will postpone a functions
        execution until after wait seconds
        have elapsed since the last time it was invoked. """

    def decorator(fn):
        def debounced(*args, **kwargs):
            def call_it():
                fn(*args, **kwargs)

            try:
                debounced.t.cancel()
            except(AttributeError):
                pass
            debounced.t = Timer(wait, call_it)
            debounced.t.start()

        return debounced

    return decorator


def throttle(mindelta):
    def decorator(fn):
        def throttled(*args, **kwargs):
            def call_it():
                fn.lastTimeExecuted = time.time()

                return fn(*args, **kwargs)

            if not hasattr(throttled, 'lastTimeExecuted'):
                # just execute fction
                try:
                    throttled.t.cancel()
                except AttributeError:
                    pass

                call_it()
                return throttled

            delta = time.time() - fn.lastTimeExecuted
            try:
                throttled.t.cancel()
            except AttributeError:
                pass

            if delta > mindelta:
                call_it()
            else:
                timespot = mindelta - delta
                throttled.t = Timer(timespot, call_it)
                throttled.t.start()

        return throttled

    return decorator


def run_async(func):
    return func

# def run_async(func):
# 	"""
#     run_async(func)
#     function decorator, intended to make "func" run in a separate
#     thread (asynchronously).
#     Returns the created Thread object
#
#     E.g.:
#     @run_async
#     def task1():
#         do_something
#
#     @run_async
#     def task2():
#         do_something_too
#
#     t1 = task1()
#     t2 = task2()
#     ...
#     t1.join()
#     t2.join()
#     """
#
# 	@wraps(func)
# 	def async_func(*args, **kwargs):
# 		func_hl = Thread(target=func, args=args, kwargs=kwargs)
# 		func_hl.start()
# 		return func_hl
#
# 	return async_func
