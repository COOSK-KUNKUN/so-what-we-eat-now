# -*- coding: UTF-8 -*-

import wx
import random

class mycoosk(wx.Frame):
    """docstring for mycoosk"""
    def __init__(self, parent,title):
        super(mycoosk, self).__init__(parent, title = title, size = (300,200) )
        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)
        box1 = wx.BoxSizer(wx.VERTICAL)
        box2 = wx.BoxSizer(wx.VERTICAL)
        label = wx.StaticText(panel , -1 , style = wx.ALIGN_CENTER)    
        
        txt = "一会吃什么，吃什么？"
       
        font = wx.Font(18, wx.SCRIPT, wx.NORMAL, wx.NORMAL) 
        label.SetFont(font) 
        label.SetLabel(txt) 

        box1.Add(label, -1, wx.ALIGN_CENTER)

        self.CreateStatusBar()

        ##########################################################################

        self.button = wx.Button(panel, -1, label = "开始！", pos = (40,50))
        box1.Add(self.button, 0, wx.ALIGN_CENTER)
        self.Bind(wx.EVT_BUTTON,self.OnClicked)

        font = self.GetFont() 
        panel.SetSizer(box)

 
        

    def OnClicked(self,event):
        print  random.choice ( ['apple', 'pear', 'peach', 'orange', 'lemon'] )
        pass
       

        


app = wx.App()

frame = mycoosk(None, 'COOSK')

frame.Show()

app.MainLoop()