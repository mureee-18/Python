import os

def AutoUpgrade():
    # アップデート対象のパッケージリスト
    target_packages = ['numpy', 'pandas']
    for package in target_packages:
        #パッケージをアップデート
        os.system(f'pip install --upgrade {package}')