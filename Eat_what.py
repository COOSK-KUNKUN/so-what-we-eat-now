# -*- coding: UTF-8 -*-

import wx
import random

class mycoosk(wx.Frame):
    """docstring for mycoosk"""
    def __init__(self, parent,title):
        super(mycoosk, self).__init__(parent, title = title, size = (250,150) )
        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)
        box1 = wx.BoxSizer(wx.VERTICAL)
 
        label = wx.StaticText(panel , -1 , style = wx.ALIGN_CENTER)    
        
        txt = "一会吃什么，吃什么？"
       
        font = wx.Font(18, wx.SCRIPT, wx.NORMAL, wx.NORMAL) 
        label.SetFont(font) 
        label.SetLabel(txt) 

        box1.Add(label, -1, wx.ALIGN_CENTER)

        self.CreateStatusBar()

        ##########################################################################

        self.button = wx.Button(panel, -1, label = "开始！", pos = (72,50))
        box1.Add(self.button, 0, wx.ALIGN_CENTER)
        self.Bind(wx.EVT_BUTTON,self.OnClicked)
        
        self.count = 0
        # 计数

        font = self.GetFont() 
        #显示字体
        panel.SetSizer(box) 
        # box 自动对齐
        self.Centre()
        

    def OnClicked(self,event):
        if self.count <= 3:
            dlg1 = wx.MessageDialog(self,random.choice ( ['炒面', '炒饭', '四川担担面', '饺子', '水煮肉片', '小酥肉', '西红柿炒鸡蛋盖浇饭', '爆葱鸡蛋盖浇饭', '热干面', '京酱面', '猪扒饭', '鸡扒饭', '宫保鸡丁盖浇饭', '鱼香肉丝盖浇饭', '红烧茄子盖浇饭', '菲菜鸡蛋盖浇饭', '糖醋里脊盖浇饭', '牛肉拉面', '麻辣烫','烩面','月亮馍','鸡丁面','刀削面','沙县小吃','学府卤肉饭','学府餐厅走一走','披萨'] ))   
            # 弹出消息框。      
            if dlg1.ShowModal() == wx.ID_OK: 
                print  'yes'
            pass
        
        self.count = self.count + 1

        if self.count >= 5:
            dlg2 = wx.MessageDialog(self, "已经随机菜单了5次了，如果还选不出要吃什么，那就饿着吧")
            if dlg2.ShowModal() == wx.ID_OK: 
                print  'no'
            return;
            pass

        pass
       

app = wx.App()

frame = mycoosk(None, 'COOSK')

frame.Show()

app.MainLoop()