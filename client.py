from funcs import *

import wx
import Frames

AvailablePeople = []

def AppendPersonToSend(Frame, name):
    AvailablePeople.append(Frames.SendToPanel( Frame.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.Size( 400,80 ), wx.TAB_TRAVERSAL ))
    Frame.bSizer5.Add( AvailablePeople[-1], 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )
    AvailablePeople[-1].SetLabel(name)
    AvailablePeople[-1].ButtonClick = SendClicked

def SendClicked(event):
    print("here")

class FileSend(Frames.FileSendFrame):
    def __init__(self, parent):
        Frames.FileSendFrame.__init__(self, parent)
        for panel in AvailablePeople:
            panel.ButtonClick = SendClicked
    def ButtonClick(self, event):
        pass
    def OnShow(self, event):
        AppendPersonToSend(self, "person")
    def FileChanged(self, event):
        pass
    def ScanNearby(self, event):
        self.bSizer5.Clear(delete_windows=True)

locale = wx.Locale.GetSystemLanguage()
app = wx.App()
app.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
f = FileSend(None)
f.Show(True)
app.MainLoop()
