import wx
class MyApp(wx.App):
    def OnInit(self):
        # メインウィンドウの作成
        frame = wx.Frame(None, title="メモアプリ", size=(400, 300))
        
        # wx.Notebookの作成
        self.notebook = wx.Notebook(frame)
        
        # タブページの作成
        self.pages = []
        for i in range(3):  # 3つのタブを作成
            page = wx.Panel(self.notebook)
            self.pages.append(page)
            self.notebook.AddPage(page, f"メモ {i + 1}")
            self.setupPage(page, i)
        
        # メインウィンドウを表示
        frame.Show()
        return True
    def setupPage(self, page, index):
        # 各ページにテキストボックスを追加
        sizer = wx.BoxSizer(wx.VERTICAL)
        text_box = wx.TextCtrl(page, style=wx.TE_MULTILINE | wx.TE_PROCESS_ENTER)
        sizer.Add(text_box, 1, wx.EXPAND | wx.ALL, 5)
        page.SetSizer(sizer)
# アプリケーションの実行
app = MyApp()
app.MainLoop()