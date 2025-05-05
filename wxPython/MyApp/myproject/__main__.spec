# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['__main__.py'],
    pathex=['D:\\vscode\\wxPython\\MyApp\\myproject'],
    binaries=[],
    datas=[],
    hiddenimports=[''],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,)
pyz = PYZ(a.pure, a.zipped_data,
            cipher=block_cipher)

#ファイル軽量化のためのコードここから
Key = ['mkl']
def remove_from_list(input, keys):
    outlist = []
    for item in input:
        name, _, _ = item
        flag = 0
        for key_word in keys:
            if name.find(key_word) > -1:
                flag = 1
        if flag != 1:
            outlist.append(item)
    return outlist
a.binaries = remove_from_list(a.binaries, Key)
#ここまで

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Excel編集アプリ',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None
)
coll = COLLECT(exe,
                a.binaries,
                a.zipfiles,
                a.datas,
                strip=False,
                upx=True,
                upx_exclude=[],
                name='__main__')