import wx
import openpyxl

class mainFrame(wx.App):
	def OnInit(self):
		frame = wx.Frame(None, title='Excel編集', size=(800,600))
		# wx.Notebookの作成
		self.notebook = wx.Notebook(frame)
		#タブページの作成
		image_list = wx.ImageList(16, 16)  # アイコンのサイズを指定 (16x16)
        
        # アイコンの作成とイメージリストへの追加
		icon1 = wx.ArtProvider.GetBitmap(wx.ART_INFORMATION, wx.ART_OTHER, (16, 16))
		icon2 = wx.ArtProvider.GetBitmap(wx.ART_WARNING, wx.ART_OTHER, (16, 16))
		image_list.Add(icon1)  # 0番目のアイコン
		image_list.Add(icon2)  # 1番目のアイコン
        
        # wx.Notebookにイメージリストを設定
		self.notebook.AssignImageList(image_list)
        
        # タブページの作成
		self.page1 = wx.Panel(self.notebook)
		self.page2 = wx.Panel(self.notebook)
        
        # タブにページを追加(アイコン付き)
		self.notebook.AddPage(self.page1, "タブ1", select=True, imageId=0)
		self.notebook.AddPage(self.page2, "タブ2", imageId=1)
        
        # 各ページにコンテンツを追加
		self.setupPage1()
		self.setupPage2()
		frame.Show()
		return True
	
	def setupPage1(self):
		sizer = wx.BoxSizer(wx.VERTICAL)
	#フォント
		self.font_Title = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
		self.font_text = wx.Font(13,wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
	#タイトルテキスト
		title_text = wx.StaticText(self.page1, label='編集するエクセルのパスを設定', style=wx.TE_CENTER, pos=(100,50))
		title_text.SetFont(self.font_Title)
	#内容
		#ファイル選択ダイアログ
		txt2 = wx.StaticText(self.page1, label='ファイル選択ダイアログから選択', style=wx.TE_CENTER, pos=(60,115))
		txt2.SetFont(self.font_text)
		self.txtbox1 = wx.TextCtrl(self.page1, value='', style=wx.TE_READONLY, pos=(300,110), size=(300,-1))
		btn2 = wx.Button(self.page1, wx.ID_ANY, '...', pos=(600,110), size=(20,-1))
		btn2.Bind(wx.EVT_BUTTON, self.clk_btn2)
		self.page1.SetSizer(sizer)
	def clk_btn2(self, event):
		sizer = wx.BoxSizer(wx.VERTICAL)
		dialog = wx.FileDialog(self.page1, 'ファイルを選択してください', wildcard='Excelファイル|*.xlsx', style=wx.FD_OPEN|wx.FD_FILE_MUST_EXIST)
		if dialog.ShowModal()==wx.ID_OK:
			self.path = dialog.GetPath()
			self.txtbox1.SetValue(self.path)
			#openpyxl
			path = self.path
			wb = openpyxl.load_workbook(f'{path}')
			sheetname_list = wb.sheetnames
			title_text = wx.StaticText(self.page1, label='シート名:', style=wx.TE_CENTER, pos=(60,180))
			title_text.SetFont(self.font_Title)
			x = 0
			for i in sheetname_list:
				txt3 = wx.StaticText(self.page1, label=f'{sheetname_list[x]}', style=wx.TE_CENTER, pos=(170,180+x*20))
				txt3.SetFont(self.font_text)
				x = x+1
		dialog.Destroy()
		self.page1.SetSizer(sizer)
	
	def setupPage2(self):
		sizer = wx.BoxSizer(wx.VERTICAL)
	#フォント
		font_Title = wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
		font_text = wx.Font(13,wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL)
	#タイトル
		
	#内容
		self.page2.SetSizer(sizer)
		

def mainapp():
	application = mainFrame()
	application.MainLoop()