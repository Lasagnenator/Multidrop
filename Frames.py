# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class FileSendFrame
###########################################################################

class FileSendFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Send File", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.RESIZE_BORDER|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

        self.ScanButton = wx.Button( self, wx.ID_ANY, u"Scan", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
        bSizer4.Add( self.ScanButton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Select file", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        bSizer4.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OPEN|wx.FLP_SMALL )
        bSizer4.Add( self.m_filePicker1, 0, wx.ALL, 5 )

        self.FileNameLabel = wx.StaticText( self, wx.ID_ANY, u"File:", wx.DefaultPosition, wx.Size( 200,-1 ), wx.ALIGN_CENTER_HORIZONTAL|wx.ST_ELLIPSIZE_MIDDLE )
        self.FileNameLabel.Wrap( -1 )

        bSizer4.Add( self.FileNameLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer6.Add( bSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,160 ), wx.HSCROLL|wx.VSCROLL )
        self.m_scrolledWindow1.SetScrollRate( 5, 5 )
        self.bSizer5 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel2 = SendToPanel( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        self.bSizer5.Add( self.m_panel2, 1, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.m_scrolledWindow1.SetSizer( self.bSizer5 )
        self.m_scrolledWindow1.Layout()
        bSizer6.Add( self.m_scrolledWindow1, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer6 )
        self.Layout()
        bSizer6.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.Bind( wx.EVT_SHOW, self.OnShow )
        self.ScanButton.Bind( wx.EVT_BUTTON, self.ScanNearby )
        self.m_filePicker1.Bind( wx.EVT_FILEPICKER_CHANGED, self.FileChanged )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def OnShow( self, event ):
        event.Skip()

    def ScanNearby( self, event ):
        event.Skip()

    def FileChanged( self, event ):
        event.Skip()


###########################################################################
## Class SendToPanel
###########################################################################

class SendToPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 400,80 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        self.ReceiverName = wx.StaticText( self, wx.ID_ANY, u"name", wx.DefaultPosition, wx.Size( 100,-1 ), wx.ALIGN_LEFT|wx.ST_ELLIPSIZE_END )
        self.ReceiverName.Wrap( -1 )

        bSizer6.Add( self.ReceiverName, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.ProgressGuage = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
        self.ProgressGuage.SetValue( 0 )
        bSizer6.Add( self.ProgressGuage, 1, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.SendButton = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,64 ), 0|wx.BORDER_NONE )

        self.SendButton.SetBitmap( wx.Bitmap( u"send.png", wx.BITMAP_TYPE_ANY ) )
        bSizer6.Add( self.SendButton, 0, wx.TOP|wx.BOTTOM, 5 )

        self.DeniedLabel = wx.StaticText( self, wx.ID_ANY, u"Denied", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.DeniedLabel.Wrap( -1 )

        self.DeniedLabel.Hide()

        bSizer6.Add( self.DeniedLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.AcceptedLabel = wx.StaticText( self, wx.ID_ANY, u"Accepted", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.AcceptedLabel.Wrap( -1 )

        self.AcceptedLabel.Hide()

        bSizer6.Add( self.AcceptedLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.SetSizer( bSizer6 )
        self.Layout()

        # Connect Events
        self.SendButton.Bind( wx.EVT_BUTTON, self.ButtonClick )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def ButtonClick( self, event ):
        event.Skip()


###########################################################################
## Class FileReceiveDialog
###########################################################################

class FileReceiveDialog ( wx.Dialog ):

    def __init__( self, parent ):
        wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = u"Incoming file", pos = wx.DefaultPosition, size = wx.DefaultSize, style = 0 )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        self.SenderNameLabel = wx.StaticText( self, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.SenderNameLabel.Wrap( -1 )

        bSizer5.Add( self.SenderNameLabel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.FileInfoLabel = wx.StaticText( self, wx.ID_ANY, u"FileName - size", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.FileInfoLabel.Wrap( -1 )

        bSizer5.Add( self.FileInfoLabel, 0, wx.ALL, 5 )


        bSizer4.Add( bSizer5, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.AcceptButton = wx.Button( self, wx.ID_ANY, u"Accept", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.AcceptButton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.DenyButton = wx.Button( self, wx.ID_ANY, u"Deny", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer4.Add( self.DenyButton, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )


        self.SetSizer( bSizer4 )
        self.Layout()
        bSizer4.Fit( self )

        self.Centre( wx.BOTH )

        # Connect Events
        self.AcceptButton.Bind( wx.EVT_BUTTON, self.AcceptFile )
        self.DenyButton.Bind( wx.EVT_BUTTON, self.DenyFile )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def AcceptFile( self, event ):
        event.Skip()

    def DenyFile( self, event ):
        event.Skip()


###########################################################################
## Class ListenerFrame
###########################################################################

class ListenerFrame ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Incoming files", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.SYSTEM_MENU|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer8 = wx.BoxSizer( wx.VERTICAL )

        self.m_scrolledWindow2 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.VSCROLL )
        self.m_scrolledWindow2.SetScrollRate( 5, 5 )
        gSizer2 = wx.GridSizer( 0, 2, 0, 0 )

        self.m_panel5 = IncomingPanel( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        gSizer2.Add( self.m_panel5, 1, wx.EXPAND |wx.ALL, 5 )


        self.m_scrolledWindow2.SetSizer( gSizer2 )
        self.m_scrolledWindow2.Layout()
        gSizer2.Fit( self.m_scrolledWindow2 )
        bSizer8.Add( self.m_scrolledWindow2, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer8 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


###########################################################################
## Class IncomingPanel
###########################################################################

class IncomingPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 250,-1 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer7 = wx.BoxSizer( wx.VERTICAL )

        bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText8 = wx.StaticText( self, wx.ID_ANY, u"Name", wx.DefaultPosition, wx.DefaultSize, wx.ST_ELLIPSIZE_END|wx.ST_NO_AUTORESIZE )
        self.m_staticText8.Wrap( -1 )

        bSizer9.Add( self.m_staticText8, 0, wx.ALL, 5 )

        self.m_staticText9 = wx.StaticText( self, wx.ID_ANY, u"Filename", wx.DefaultPosition, wx.DefaultSize, wx.ST_ELLIPSIZE_MIDDLE|wx.ST_NO_AUTORESIZE )
        self.m_staticText9.Wrap( -1 )

        bSizer9.Add( self.m_staticText9, 0, wx.ALL, 5 )

        self.m_staticText10 = wx.StaticText( self, wx.ID_ANY, u"Size", wx.DefaultPosition, wx.DefaultSize, wx.ST_NO_AUTORESIZE )
        self.m_staticText10.Wrap( -1 )

        bSizer9.Add( self.m_staticText10, 0, wx.ALL, 5 )


        bSizer7.Add( bSizer9, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_button5 = wx.Button( self, wx.ID_ANY, u"Deny", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
        bSizer10.Add( self.m_button5, 0, wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_button7 = wx.Button( self, wx.ID_ANY, u"Accept", wx.DefaultPosition, wx.DefaultSize, wx.BU_EXACTFIT )
        bSizer10.Add( self.m_button7, 0, wx.ALIGN_CENTER_VERTICAL, 5 )


        bSizer7.Add( bSizer10, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )


        self.SetSizer( bSizer7 )
        self.Layout()

    def __del__( self ):
        pass


