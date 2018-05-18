# Kodi add-on: script.service.cle0
# 2018-05-11 by clerfayt

import xbmcaddon
import xbmcgui
import subprocess

from resources.lib.utils import *

dlg = xbmcgui.Dialog()
com = dlg.select(transl(30011), [MySettings.commandLabel1(), MySettings.commandLabel2(),
                                 MySettings.commandLabel3(), MySettings.commandLabel4(),
                                 MySettings.commandLabel5()])

commands = [MySettings.commandString1(), MySettings.commandString2(), MySettings.commandString3(),
            MySettings.commandString4(), MySettings.commandString5()]

if ((com >= 0 and com < len(commands)) and commands[com]):
    #only execute if commands[com] is not empty
    try:
        subprocess.Popen(args=commands[com].split(" "))
    except OSError as err:
        myLog("The specified command (" + commands[com] + ") yielded an error! OSError: {0}".format(err))
