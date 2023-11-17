# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=['C:\\Users\\id4rk\\PycharmProjects\\yandexProject'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

a.datas += [('saved_account.csv', 'C:\\Users\\id4rk\\PycharmProjects\\yandexProject\\saved_account.csv', 'DATA')]
a.datas += [('copy.png', 'C:\\Users\\id4rk\\PycharmProjects\\yandexProject\\icons\\copy.png', 'DATA')]
a.datas += [('create_new_dir.png', 'C:\\Users\id4rk\\PycharmProjects\\yandexProject\\icons\\create_new_dir.png', 'DATA')]
a.datas += [('create_new_file.png', 'C:\\Users\\id4rk\\PycharmProjects\\yandexProject\\icons\\create_new_file.png', 'DATA')]
a.datas += [('cut.png', 'C:\\Users\\id4rk\\PycharmProjects\\yandexProject\\icons\\cut.png', 'DATA')]
a.datas += [('delete.png', 'C:\\Users\\id4rk\\PycharmProjects\\yandexProject\\icons\\delete.png', 'DATA')]
a.datas += [('edit_path.png', 'C:\\Users\\id4rk\\PycharmProjects\\yandexProject\\icons\\edit_path.png', 'DATA')]
a.datas += [('find.png', 'C:\\Users\\id4rk\\PycharmProjects\\yandexProject\\icons\\find.png', 'DATA')]
a.datas += [('move_back.png', 'C:\\Users\\id4rk\\PycharmProjects\\yandexProject\\icons\\move_back.png', 'DATA')]
a.datas += [('move_forward.png', 'C:\\Users\\id4rk\\PycharmProjects\\yandexProject\\icons\\move_forward.png', 'DATA')]
a.datas += [('move_homepage.png', 'C:\\Users\\id4rk\\PycharmProjects\\yandexProject\\icons\\move_homepage.png', 'DATA')]
a.datas += [('move_to_my_computer.png', 'C:\\Users\id4rk\\PycharmProjects\\yandexProject\\icons\\move_to_my_computer.png', 'DATA')]
a.datas += [('move_up.png', 'C:\\Users\\id4rk\\PycharmProjects\\yandexProject\\icons\\move_up.png', 'DATA')]
a.datas += [('open.png', 'C:\\Users\\id4rk\\PycharmProjects\\yandexProject\\icons\\open.png', 'DATA')]
a.datas += [('paste.png', 'C:\\Users\\id4rk\\PycharmProjects\\yandexProject\\icons\\paste.png', 'DATA')]
a.datas += [('rename.png', 'C:\\Users\\id4rk\\PycharmProjects\\yandexProject\\icons\\rename.png', 'DATA')]
a.datas += [('settings.png', 'C:\\Users\id4rk\PycharmProjects\yandexProject\icons\\settings.png', 'DATA')]
a.datas += [('user.png', 'C:\\Users\\id4rk\\PycharmProjects\\yandexProject\\icons\\user.png', 'DATA')]
a.datas += [('admin.jpg', 'C:\\Users\\id4rk\\PycharmProjects\\yandexProject\\images\\admin.jpg', 'DATA')]
a.datas += [('user.jpg', 'C:\\Users\\id4rk\\PycharmProjects\\yandexProject\\images\\user.jpg', 'DATA')]

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
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
    entitlements_file=None,
)
