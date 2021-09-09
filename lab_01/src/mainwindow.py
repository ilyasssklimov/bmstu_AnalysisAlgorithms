from algorithm import Algorithm
from design import Ui_MainWindow
from PyQt5 import QtWidgets
import matplotlib
import matplotlib.pyplot as plt
import random
import string


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Расстояние Левенштейна')

        self.algorithms = {
            'lev_mat': Algorithm('levenshtein_matrix'),
            'lev_rec': Algorithm('levenshtein_recursively'),
            'lev_rec_cache': Algorithm('levenshtein_recursively_cache'),
            'dam_lev': Algorithm('damerau_levenshtein')
        }
        self.cur_algorithm = 'lev_mat'

        self.lev_mat.setChecked(True)
        self.lev_mat.clicked.connect(lambda: self.change_algorithm('lev_mat'))
        self.lev_rec.clicked.connect(lambda: self.change_algorithm('lev_rec'))
        self.lev_rec_cache.clicked.connect(lambda: self.change_algorithm('lev_rec_cache'))
        self.dam_lev.clicked.connect(lambda: self.change_algorithm('dam_lev'))

        self.edit_str_1.textChanged.connect(self.init_result_string)
        self.edit_str_2.textChanged.connect(self.init_result_string)

        self.search.clicked.connect(self.get_distance)

        matplotlib.use('Qt5Agg')
        self.graph_lev_rec.clicked.connect(self.graphics_lev_rec)

    def change_algorithm(self, new_algorithm):
        self.cur_algorithm = new_algorithm

    def init_result_string(self):
        self.result_string.setText('Редакционное расстояние = ?')

    def get_distance(self):
        distance = self.algorithms[self.cur_algorithm].execute(
            self.edit_str_1.text(), self.edit_str_2.text()
        )
        self.result_string.setText(f'Редакционное расстояние = {distance}')

    def graphics_lev_rec(self):
        x_lev_mat = []
        x_lev_rec_cache = []
        y = []
        letters = string.ascii_lowercase
        # name='График зависимости времени от размерности строк'
        for n in range(10, 101, 10):
            str_1 = ''.join(random.choice(letters) for _ in range(n))
            str_2 = ''.join(random.choice(letters) for _ in range(n))

            x_lev_mat.append(self.algorithms['lev_mat'].get_time(str_1, str_2))
            x_lev_rec_cache.append(self.algorithms['lev_rec_cache'].get_time(str_1, str_2))
            y.append(n)

        plt.plot(x_lev_mat, y, marker='o', color='red', label='Левенштейн - матрично')
        plt.plot(x_lev_rec_cache, y, marker='o', color='green', label='Левенштейн - рекурсвино с кэшем')
        plt.legend()
        plt.show()



