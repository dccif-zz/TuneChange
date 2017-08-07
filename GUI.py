# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class TuneChangeGui
###########################################################################

class TuneChangeGui(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"TuneChange", pos=wx.DefaultPosition,
                          size=wx.Size(800, 500), style=wx.CAPTION | wx.CLOSE_BOX | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        self.SetBackgroundColour(wx.Colour(242, 242, 242))

        Mainlayout = wx.BoxSizer(wx.VERTICAL)

        self.Breif = wx.StaticText(self, wx.ID_ANY, u"数字前0表示低音  (e.g. #05 ->低半音乐5)\n重复数字表示高音  (e.g. #33->高半音3)\n输入:请用空格或者逗号分隔 所有半音用#表示",
                                   wx.DefaultPosition, wx.Size(-1, 70), 0)
        self.Breif.Wrap(-1)
        self.Breif.SetFont(wx.Font(14, 70, 90, 90, False, wx.EmptyString))

        Mainlayout.Add(self.Breif, 0, wx.EXPAND | wx.TOP | wx.BOTTOM | wx.LEFT, 3)

        ChoiceBar = wx.BoxSizer(wx.HORIZONTAL)

        #ChoiceBar.SetMinSize(wx.Size(10, -1))
        Choice1Choices = [u"G", u"#G/Ab", u"A", u"#A/Bb", u"B", u"C", u"#C/Db", u"D", u"#D/Eb", u"E", u"F", u"#F"]
        self.Choice1 = wx.Choice(self, wx.ID_ANY, wx.Point(-1, -1), wx.Size(60, 30), Choice1Choices, 0)
        self.Choice1.SetSelection(5)
        ChoiceBar.Add(self.Choice1, 0, wx.ALL, 5)

        ChoiceBar.AddSpacer(350)

        Choice2Choices = [u"G", u"#G/Ab", u"A", u"#A/Bb", u"B", u"C", u"#C/Db", u"D", u"#D/Eb", u"E", u"F", u"#F"]
        self.Choice2 = wx.Choice(self, wx.ID_ANY, wx.Point(-1, -1), wx.Size(60, 30), Choice2Choices, 0)
        self.Choice2.SetSelection(5)
        ChoiceBar.Add(self.Choice2, 0, wx.ALL, 5)

        Mainlayout.Add(ChoiceBar, 0, wx.ALL | wx.EXPAND, 2)

        ChangeArea = wx.BoxSizer(wx.HORIZONTAL)

        self.Before = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(350, -1),
                                  wx.TE_AUTO_URL|wx.TE_LEFT | wx.TE_MULTILINE)
        self.Before.SetFont(wx.Font(14, 70, 90, 90, False, wx.EmptyString))
        ChangeArea.Add(self.Before, 0, wx.ALL | wx.EXPAND, 5)

        ButtonArea = wx.BoxSizer(wx.VERTICAL)

        ButtonArea.AddSpacer(50)

        self.Change = wx.Button(self, wx.ID_ANY, u"转换->", wx.DefaultPosition, wx.DefaultSize, 0)
        ButtonArea.Add(self.Change, 0, wx.ALL, 5)

        ButtonArea.AddSpacer(40)

        self.Clear = wx.Button(self, wx.ID_ANY, u"清空", wx.DefaultPosition, wx.DefaultSize, 0)
        ButtonArea.Add(self.Clear, 0, wx.ALL, 5)

        ButtonArea.AddSpacer(0)

        ChangeArea.Add(ButtonArea, 1, wx.EXPAND, 5)

        self.After = wx.TextCtrl(self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(350, -1),
                                 wx.TE_AUTO_URL | wx.TE_LEFT | wx.TE_MULTILINE | wx.TE_READONLY)
        self.After.SetFont(wx.Font(14, 70, 90, 90, False, wx.EmptyString))
        ChangeArea.Add(self.After, 0, wx.ALL | wx.EXPAND, 5)

        Mainlayout.Add(ChangeArea, 1, wx.EXPAND, 5)

        self.SetSizer(Mainlayout)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Choice1.Bind(wx.EVT_CHOICE, self.BeforeChoice)
        self.Choice2.Bind(wx.EVT_CHOICE, self.AfterChoice)
        self.Change.Bind(wx.EVT_BUTTON, self.ChangeStart)
        self.Clear.Bind(wx.EVT_BUTTON, self.ClearAll)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def BeforeChoice(self, event):
        event.Skip()

    def AfterChoice(self, event):
        event.Skip()

    def ChangeStart(self, event):
        event.Skip()

    def ClearAll(self, event):
        event.Skip()

