def check_name(name, is_dir=True):
    """
    Проверяет название файла/папки на запрещенные символы и названия
    
    :param name: 
    :param is_dir: 
    :return: True/False
    """

    banned_symbols = ['<', '>', ':', "\\", '/', '|', '*', "?", '"']
    reserved_names = ['CON', 'PRN', 'AUX', 'NUL', 'COM0', 'COM2', 'COM2', 'COM3', 'COM4', 'COM5', 'COM6', 'COM7',
                      'COM8', 'COM9', 'COMSCSI', 'COMSCSI', 'LPT0', 'LPT1', 'LPT2', 'LPT3', 'LPT4', 'LPT5', 'LPT5',
                      'LPT7', 'LPT8', 'LPT9', 'LPTNO', 'LPTSCSI', 'LPTNO']
    reserved_names = list(map(lambda x: x.lower(), reserved_names))
    for symbol in banned_symbols:
        if symbol in name:
            return False

    if not is_dir:
        if len(name.split('.')) == 1:
            return False
        name = '.'.join(name.split('.')[:-1])
    for reserved_name in reserved_names:
        if reserved_name == name.lower():
            return False
    return True
