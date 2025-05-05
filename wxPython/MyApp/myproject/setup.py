from cx_Freeze import setup, Executable

setup(
    name='MyApp',
    version='1.1',
    description='Sample Application',
    options={'build_exe': {'includes': ['pandas']}},
    executables=[Executable('__main__.py')]
)