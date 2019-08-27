from funcs import *

import wx
import Frames
import os
import time

AvailablePeople = []
scan_results = [0]

def AppendPersonToSend(Frame, name):
    AvailablePeople.append(Frames.SendToPanel( Frame.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL ))
    Frame.bSizer5.Add( AvailablePeople[-1], 1, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 5 )
    AvailablePeople[-1].ReceiverName.SetLabel(name)
    AvailablePeople[-1].SendButton.Bind(wx.EVT_BUTTON, SendClicked)

def SendClicked(event):
    #get the index of the person in the list
    index = AvailablePeople.index(event.EventObject.Parent)

def ScanNearby(self):
    global scan_results
    scan_results = ["here"]
    #print("here")
    scan_results = scan()
    #scan_results = scan2()
    for result in scan_results:
        name = result[1]
        addr = result[0]
        AppendPersonToSend(self, name)
        pass

class FileSend(Frames.FileSendFrame):
    def __init__(self, parent):
        Frames.FileSendFrame.__init__(self, parent)
    def OnShow(self, event):
        #testing, this will be moved to 
        AppendPersonToSend(self, "person1")
        AppendPersonToSend(self, "person2")
    def FileChanged(self, event):
        fname = os.path.basename(self.m_filePicker1.Value)
        self.FileNameLabel.SetValue(fname)
        pass
    def ScanNearby(self, event):
        #clear the available people
        self.bSizer5.Clear(delete_windows=True)
        #run this in a thread to allow other things to run.
        #give it the 'self' argument to let it update the
        #window with the results so no callback is needed.
        ScanNearby(self)
        #print("here")
        run_in_thread(ScanNearby, [0], 0, self)

locale = wx.Locale.GetSystemLanguage()
app = wx.App()
app.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
f = FileSend(None)
f.Show(True)
app.MainLoop()
