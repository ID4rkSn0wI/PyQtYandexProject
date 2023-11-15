from utils.parsePath import parse_path


def return_index_and_path(self):
    """
    Возвращает индекс и путь из нужного QTreeView.

    :param self: QMainWindow
    :return: index: QModelIndex, path: str
    """

    if self.where == 1:
        index = self.dirView.currentIndex()
        path = self.dirModel.filePath(index)
    elif self.where == 2:
        index = self.fileView.currentIndex()
        path = self.fileModel.filePath(index)
        if ('/'.join(parse_path(path).split('/')[:-1]) + ('/' if len(parse_path(path).split('/')) == 2 else '')
                != parse_path(self.cur_path)):
            path = self.cur_path
            index = self.fileModel.index(path)
    return index, parse_path(path)
