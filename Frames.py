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
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Send File", pos = wx.DefaultPosition, size = wx.Size( 800,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

        bSizer6 = wx.BoxSizer( wx.VERTICAL )

        bSizer4 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"Select file", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )

        bSizer4.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_OPEN|wx.FLP_SMALL )
        bSizer4.Add( self.m_filePicker1, 0, wx.ALL, 5 )


        bSizer6.Add( bSizer4, 0, wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_scrolledWindow1 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
        self.m_scrolledWindow1.SetScrollRate( 5, 5 )
        bSizer5 = wx.BoxSizer( wx.VERTICAL )

        self.m_panel1 = SendToPanel( self.m_scrolledWindow1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
        bSizer5.Add( self.m_panel1, 0, wx.ALL, 5 )


        self.m_scrolledWindow1.SetSizer( bSizer5 )
        self.m_scrolledWindow1.Layout()
        bSizer5.Fit( self.m_scrolledWindow1 )
        bSizer6.Add( self.m_scrolledWindow1, 1, wx.EXPAND |wx.ALL, 5 )


        self.SetSizer( bSizer6 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


###########################################################################
## Class SendToPanel
###########################################################################

class SendToPanel ( wx.Panel ):

    def __init__( self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size( 400,80 ), style = wx.TAB_TRAVERSAL, name = wx.EmptyString ):
        wx.Panel.__init__ ( self, parent, id = id, pos = pos, size = size, style = style, name = name )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        self.ReceiverName = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.TE_READONLY|wx.BORDER_DEFAULT )
        bSizer6.Add( self.ReceiverName, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.ProgressGuage = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
        self.ProgressGuage.SetValue( 0 )
        bSizer6.Add( self.ProgressGuage, 1, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_button5 = wx.Button( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 64,64 ), 0|wx.BORDER_NONE )

        self.m_button5.SetBitmap( wx.Bitmap( u"send.png", wx.BITMAP_TYPE_ANY ) )
        bSizer6.Add( self.m_button5, 0, wx.ALL, 5 )


        self.SetSizer( bSizer6 )
        self.Layout()

    def __del__( self ):
        pass


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


