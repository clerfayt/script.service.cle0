#!/bin/python
# -*- coding: utf-8 -*-

import xbmc, xbmcaddon, xbmcgui
#import os.path

ADDON = xbmcaddon.Addon()
ADDONNAME = ADDON.getAddonInfo("name")
#ADDONFOLDER = ADDON.getAddonInfo("path")


def transl(translationId):
    """Returns the translated string with the given id."""
    return ADDON.getLocalizedString(translationId).encode("utf-8")


def myNotify(message, header=None, time_=3000, icon=None, sound=True):
    """Send notification. If header==None the addon-name is used.
       If icon==None the addon-icon is used.
    """
    header = ADDONNAME if not header else header
    icon   = ADDON.getAddonInfo('icon') if not icon else icon
    xbmcgui.Dialog().notification(header, message, icon, time_, sound)

def myNotifyError(message, header=None, time_=3000, sound=True):
    myNotify(message, header, time_, xbmcgui.NOTIFICATION_ERROR, sound)

def myNotifyWarning(message, header=None, time_=3000, sound=True):
    myNotify(message, header, time_, xbmcgui.NOTIFICATION_WARNING, sound)

def myNotifyInfo(message, header=None, time_=3000, sound=True):
    myNotify(message, header, time_, xbmcgui.NOTIFICATION_INFO, sound)


def myLog(message, level=xbmc.LOGNOTICE):
    """Log a message."""
    output = "[cle0]: " + message
    xbmc.log(msg=output, level=level)


class MySettings:
    """Helper class with static methods for retrieving settings values."""
    _addon = xbmcaddon.Addon()
    @staticmethod
    def commandLabel1():
        return MySettings._addon.getSetting("comlabel1")
    @staticmethod
    def commandString1():
        return MySettings._addon.getSetting("command1")
    @staticmethod
    def commandLabel2():
        return MySettings._addon.getSetting("comlabel2")
    @staticmethod
    def commandString2():
        return MySettings._addon.getSetting("command2")
    @staticmethod
    def commandLabel3():
        return MySettings._addon.getSetting("comlabel3")
    @staticmethod
    def commandString3():
        return MySettings._addon.getSetting("command3")
    @staticmethod
    def commandLabel4():
        return MySettings._addon.getSetting("comlabel4")
    @staticmethod
    def commandString4():
        return MySettings._addon.getSetting("command4")
    @staticmethod
    def commandLabel5():
        return MySettings._addon.getSetting("comlabel5")
    @staticmethod
    def commandString5():
        return MySettings._addon.getSetting("command5")

