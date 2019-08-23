from funcs import *

import wx
import Frames

class FileSend(Frames.FileSendFrame):
    def __init__(self, parent):
        Frames.FileSendFrame.__init__(self, parent)

locale = wx.Locale.GetSystemLanguage()
app = wx.App()
app.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
f = FileSend(None)
f.Show(True)
app.MainLoop()
