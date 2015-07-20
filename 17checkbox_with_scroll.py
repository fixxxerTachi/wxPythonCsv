#-*- coding: cp932 -*-
import csv
import codecs
import wx
targetList=[1,2,3]
targetList1={
        1:'first',
        2:'second',
        3:'third'
    }
from test_sqlalchemy import users

class CustomFrame(wx.Frame):
    def __init__(self,title):
        wx.Frame.__init__(self,None,-1,title,size=(800,500))
        panel = wx.Panel(self)
        panel.SetBackgroundColour(wx.RED)
        layout = wx.BoxSizer(wx.VERTICAL)

        scrolledWindow = wx.ScrolledWindow(panel,wx.ID_ANY,style=wx.SUNKEN_BORDER)
        scrolledWindow.SetBackgroundColour(wx.WHITE)
        scrolledWindow.SetScrollbars(10,10,80,50)

        for k,v in targetList1.items():
            sub_layout = wx.BoxSizer(wx.HORIZONTAL)
            checkBox = wx.CheckBox(scrolledWindow,k,'checkbox' + str(k))
            text = wx.StaticText(scrolledWindow,wx.ID_ANY,v)
            sub_layout.Add(checkBox)
            sub_layout.Add(text) 
            layout.Add(sub_layout)

        '''
        for u in users:
            sub_layout = wx.BoxSizer(wx.HORIZONTAL)
            checkBox = wx.CheckBox(scrolledWindow,u.id,str(u.id))
            if u.del_flag == 0:
                checkBox.SetValue(True)
            text = wx.StaticText(scrolledWindow,wx.ID_ANY,u.name)
            sub_layout.Add(checkBox)
            sub_layout.Add(text)
            layout.Add(sub_layout)
        '''

        text = wx.StaticText(panel,wx.ID_ANY,u'ユーザー一覧')
        button1 = wx.Button(panel,wx.ID_ANY,'Action')
        button1.Bind(wx.EVT_BUTTON,self.DoAction)
        layout.Add(text,flag=wx.EXPAND)
        layout.Add(scrolledWindow,proportion = 1,flag= wx.EXPAND)
        layout.Add(button1,flag=wx.EXPAND)
        panel.SetSizer(layout)
        self.Show()

    def DoAction(self,event):
        for u in users:
            target = self.FindWindowById(u.id)
            if target != None:
                print target.GetLabel(), target.GetValue(), target.GetId()
        
        csvFile = codecs.open("./test.csv","w","cp932")
        writer = csv.writer(csvFile,CustomFormat())
        for u in users:
            row = (u.id,u.name,u.fullname)
            writer.writerow(row)
        csvFile.close()

class CustomFormat(csv.excel):
    quoting = csv.QUOTE_ALL

app = wx.App(False)
CustomFrame('checkbox')
app.MainLoop()
