import wx,os,csv
class CustomFrame(wx.Frame):
    def __init__(self,title):
        wx.Frame.__init__(self,None,wx.ID_ANY,title,size=(400,400))
        panel = wx.Panel(self)
        button = wx.Button(panel,wx.ID_ANY,'open')
        button.Bind(wx.EVT_BUTTON,self.OnOpen)
        
        layout = wx.BoxSizer(wx.VERTICAL)
        layout.Add(button)

        panel.SetSizer(layout)
        self.Show()

    def OnOpen(self,event):
        self.dirname=''
        dlg = wx.FileDialog(self,'choose a file',self.dirname,'','*.*',wx.OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            self.fileName = dlg.GetFilename()
            self.dirName = dlg.GetDirectory()
            file = open(os.path.join(self.dirName,self.fileName),'rb')
            dataReader = csv.reader(file)
            for row in dataReader:
                print row
            file.close()
        dlg.Destroy()

app = wx.App(False)
CustomFrame('wx.Frame')
app.MainLoop()
