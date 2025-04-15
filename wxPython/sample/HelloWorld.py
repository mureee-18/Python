import wx

# メインフレームクラス
class SampleFrame(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, title=title, pos=(0, 0), size=(320, 240))
        self.__create_widget()
        self.__do_layout()

    # Widgetを作成するメソッド
    def __create_widget(self):
        # Hello WorldのテキストWidget作成
        self.text = wx.StaticText(self, label="Hello World", pos=wx.Point(50, 20))

    # レイアウトを設定するメソッド
    def __do_layout(self):
        # レイアウトの設定
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.text)
        self.SetSizer(sizer)

# アプリケーションクラス
class SampleApp(wx.App):
    # wxPythonのアプリケーションクラスの初期化にはOnInitメソッドを使用する
    def OnInit(self):
        # フレームのオブジェクト生成
        frame = SampleFrame(None, -1, "Sample wxPython")
        # メインフレームに設定
        self.SetTopWindow(frame)
        # フレームの表示
        frame.Show(True)
        return True

if __name__ == '__main__':
    # アプリケーションオブジェクトの生成
    app = SampleApp()
    # メインループ
    app.MainLoop()