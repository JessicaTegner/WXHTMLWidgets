from re import I
import wx
import wx.html2

class AccessibleHTMLDialog(wx.Dialog):
    def __init__(self, parent, id, title, style=wx.DEFAULT_DIALOG_STYLE):
        wx.Dialog.__init__(self, parent, id, title, style=style)
        self.html = wx.html2.WebView.New(self)
        self.buttonSizer = wx.BoxSizer(wx.HORIZONTAL)
        self.focuser = wx.UIActionSimulator()
        wx.CallAfter(self.focuser.MouseMove, self.html.GetScreenPosition())
        wx.CallAfter(self.focuser.MouseClick) 
        self.html.Bind(wx.EVT_SET_FOCUS, self.OnSetFocus)
        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(self.html, 1, wx.EXPAND)
        mainSizer.Add(self.buttonSizer, flag=wx.ALIGN_CENTER|wx.TOP, border=15)
        self.SetSizer(mainSizer)
        self.Centre()

    def SetPage(self, text):
        self.html.SetPage(text, "")
        return self

    def GetContentWindow(self):
        return self.html

    def AddButton(self, label, buttonIdentifier):
        if not isinstance(buttonIdentifier, int):
            raise TypeError("buttonIdentifier must be an integer")
        button = wx.Button(self, label=label)
        self.buttonSizer.Add(button, 0, wx.ALL, 5)
        self.Bind(wx.EVT_BUTTON, lambda event: self.DoButtonClick(event, buttonIdentifier), button)
        return self

    def DoButtonClick(self, event, buttonIdentifier):
        self.EndModal(buttonIdentifier)

    def OnSetFocus(self, event):
        wx.CallAfter(self.focuser.MouseMove, self.html.GetScreenPosition())
        wx.CallAfter(self.focuser.MouseClick) 
        event.Skip()
