import sqlite3
import sys

import matplotlib.pyplot as plt
import xlsxwriter
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFileDialog
from matplotlib.backends.backend_qt5 import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from employers import CreateNewEmployer
from grades_design import Ui_MainWindow
from position import CreateNewPosition

style_sheet = """
QPushButton#pushButton {font-size: 18px; border-radius: 5px; padding: 6px; background-color: #F5AF9B}
QPushButton#pushButton:hover {background-color: #F56D54}
QPushButton#pushButton_2 {font-size: 18px; border-radius: 5px; padding: 6px; background-color: #9BC9F5}
QPushButton#pushButton_2:hover {background-color: #74ADF5}
QPushButton#pushButton_3 {font-size: 18px; border-radius: 5px; padding: 6px; background-color: #BDF5AE}
QPushButton#pushButton_3:hover {background-color: #6FF584}
QPushButton#pushButton_4 {font-size: 18px; border-radius: 5px; padding: 6px; background-color: #F5EC7D}
QPushButton#pushButton_4:hover {background-color: #F5B04C}
#textEdit {font-size: 30px}
#textEdit_2 {font-size: 30px}
#label {font-size: 30px}"""


class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox.currentIndexChanged.connect(self.currency_fn)
        self.comboBox_2.currentIndexChanged.connect(self.currency_fn)
        self.textEdit.textChanged.connect(self.currency_fn)
        self.pushButton.clicked.connect(self.plotGraph)
        self.pushButton_10.setEnabled(False)
        self.pushButton_2.clicked.connect(self.makeReport)
        self.pushButton_3.clicked.connect(self.createNewEmployer)
        self.pushButton_4.clicked.connect(self.createNewPosition)
        self.pushButton_10.clicked.connect(self.plotEmploy)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)

        layout = QVBoxLayout(self.widget)
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        con = sqlite3.connect('grades.db')
        cur = con.cursor()
        self.res_empl = cur.execute("""SELECT * FROM employers""").fetchall()
        self.res_pos = cur.execute("""SELECT * FROM positions""").fetchall()
        self.curr = cur.execute("""SELECT * FROM conversion""").fetchall()
        con.close()
        self.plotGraph()
        self.currency_data = {}
        for el in self.curr:
            self.currency_data[el[0]] = el[1:]
        try:
            con = sqlite3.connect('grades.db')
            cur = con.cursor()
            rub = requests.get('https://v6.exchangerate-api.com/v6/b371e9a19423846531821c22/latest/RUB').json()
            usd = requests.get('https://v6.exchangerate-api.com/v6/b371e9a19423846531821c22/latest/USD').json()
            eur = requests.get('https://v6.exchangerate-api.com/v6/b371e9a19423846531821c22/latest/EUR').json()
            gbp = requests.get('https://v6.exchangerate-api.com/v6/b371e9a19423846531821c22/latest/GBP').json()
            self.currency_data['RUB'] = (
                rub['conversion_rates']['GBP'], rub['conversion_rates']['EUR'], 1, rub['conversion_rates']['USD'])
            self.currency_data['USD'] = (
                usd['conversion_rates']['GBP'], usd['conversion_rates']['EUR'], usd['conversion_rates']['RUB'], 1)
            self.currency_data['EUR'] = (
                eur['conversion_rates']['GBP'], 1, eur['conversion_rates']['RUB'], eur['conversion_rates']['USD'])
            self.currency_data['GBP'] = (
                1, gbp['conversion_rates']['EUR'], gbp['conversion_rates']['RUB'], gbp['conversion_rates']['USD'])
            cur.execute("""UPDATE conversion SET gbp = ?, eur = ?, rub = ?, usd = ? WHERE currency = 'RUB'""",
                        self.currency_data['RUB'])
            cur.execute("""UPDATE conversion SET gbp = ?, eur = ?, rub = ?, usd = ? WHERE currency = 'USD'""",
                        self.currency_data['USD'])
            cur.execute("""UPDATE conversion SET gbp = ?, eur = ?, rub = ?, usd = ? WHERE currency = 'EUR'""",
                        self.currency_data['EUR'])
            cur.execute("""UPDATE conversion SET gbp = ?, eur = ?, rub = ?, usd = ? WHERE currency = 'GBP'""",
                        self.currency_data['GBP'])
            con.commit()
            con.close()
        except Exception:
            self.label_46.setText('Ошибка подключения!')

    def currency_fn(self):
        cur = self.currency_data['RUB'][:]

        if self.comboBox.currentText() == "USD":
            cur = self.currency_data['USD'][:]
        if self.comboBox.currentText() == "EUR":
            cur = self.currency_data['EUR'][:]
        if self.comboBox.currentText() == "GBP":
            cur = self.currency_data['GBP'][:]

        ind = 3
        if self.comboBox_2.currentText() == "RUB":
            ind = 2
        if self.comboBox_2.currentText() == "EUR":
            ind = 1
        if self.comboBox_2.currentText() == "GBP":
            ind = 0

        res = cur[ind]
        res_2 = res * float(self.textEdit.toPlainText())
        self.label.setText(str(round(res_2, 4)))

    def createNewEmployer(self):
        self.create_dialog_1 = CreateNewEmployer()
        self.create_dialog_1.show()

    def createNewPosition(self):
        self.create_dialog_2 = CreateNewPosition()
        self.create_dialog_2.show()

    def plotGraph(self):
        ps = [(x[3], x[2]) for x in sorted(self.res_pos, key=lambda el: el[2])]
        n = self.spinBox.value()
        empl = [(x[5], x[6]) for x in sorted(self.res_empl, key=lambda el: el[6])]
        int = (empl[len(empl) - 1][1] - empl[0][1]) / n
        self.int = int
        box_plot_data = []
        pos_data = []
        lb = []
        for i in range(1, n + 1):
            lb.append(str(round(empl[0][1] + (i - 1) * int)) + '-' + str(round(empl[0][1] + i * int)))
            data = list(filter(lambda el: empl[0][1] + (i - 1) * int < el[1] <= empl[0][1] + i * int, empl))
            box_plot_data.append([el[0] for el in data])
            pos = list(filter(lambda el: empl[0][1] + (i - 1) * int < el[1] <= empl[0][1] + i * int, ps))
            pos_data.append([el[0] for el in pos])

        for i in range(len(pos_data)):
            if bool(pos_data[i]):
                pos_data[i] = round(sum(pos_data[i]) / len(pos_data[i]))

        self.figure.clear()
        ax = self.figure.add_subplot()  # 111
        ax.boxplot(box_plot_data, widths=[1] * n, labels=lb)
        x_pos = []
        for i in range(1, n + 1):
            x_pos.append(i * bool(pos_data[i - 1]))
        res_pos = []
        for i in range(n):
            if x_pos[i] == 0:
                continue
            res_pos.append((x_pos[i], pos_data[i]))
        ax.plot([el[0] for el in res_pos], [el[1] for el in res_pos], label=' Рыночная кривая ')
        ax.set_ylabel('    Зарплата   ',
                      fontsize=14,
                      color='black',
                      )
        ax.set_xlabel('    Коэф. Зн.   ',
                      fontsize=14,
                      color='black',
                      )
        plt.grid()
        plt.legend(loc='best')
        self.canvas.draw()
        self.rp = res_pos.copy()

    def plotEmploy(self):
        self.figure.clear()
        self.plotGraph()
        c1 = self.lineEdit_20.text().strip().capitalize()  # Фамилия
        c2 = self.lineEdit_21.text().strip().capitalize()  # Имя
        c3 = self.lineEdit_22.text().strip().capitalize()  # Отчеств
        employ = list(filter(lambda x: x[1] == c1 and x[2] == c2 and x[3] == c3, self.res_empl))
        if bool(employ):
            x, y = employ[0][6], employ[0][5]
            self.label_44.setText(f'Коэф. Зн. : {x}')
            self.label_45.setText(f'Зар. плата : {y}')
            x = x / (self.int)
            plt.scatter(x, y, label=' Сотрудник ', color='red')
            plt.legend(loc='best')
            self.canvas.draw()
            text = list(filter(lambda x: x[0] == c1 and x[1] == c2 and x[2] == c3, self.report_data))
            text = text[0][-1]
            self.label_46.setText(text)

        else:
            self.label_46.setText('Отчет: Сотрудник не найден!')

    def makeReport(self):

        file = QFileDialog.getSaveFileName(None, 'Save Excel file', "", 'Excel files (*.xlsx)')
        if file[0] == '':
            return

        def exlwrite(self):

            pos = [(el[2], el[3]) for el in sorted(self.res_pos, key=lambda x: x[2])]
            elements = list(set([x[0] for x in pos]))
            elements.sort()
            graf = []
            for el in elements:
                ems = list(filter(lambda x: x[0] == el, pos))
                avr = sum([x[1] for x in ems]) / len(ems)
                graf.append((el, avr))
            koef = []
            for i in range(len(graf) - 1):
                k = (graf[i + 1][1] - graf[i][1]) / (graf[i + 1][0] - graf[i][0])
                b = graf[i][1] - k * graf[i][0]
                koef.append((graf[i][0], k, b))
            self.report_data = [['Фамилия', 'Имя', 'Отчество', 'Должность', 'Оклад (руб)', 'Коэф. Зн.', 'Отчет']]
            for i in range(len(self.res_empl)):
                data = []
                for j in range(1, 7):
                    data.append(self.res_empl[i][j])
                compare = list(filter(lambda x: x[0] <= data[5], koef))
                compare = compare[-1]
                c = compare[1] * data[5] + compare[2]
                if data[4] > c:
                    pers = 100 * (data[4] - c) / c
                    data.append(f'З.п. выше рынка на {int(pers)}%')
                elif data[4] == c:
                    data.append(f'З.п. по рынку')
                else:
                    pers = 100 * (c - data[4]) / data[4]
                    data.append(f'З.п. ниже рынка на {int(pers)}%')
                self.report_data.append(data)

        exlwrite(self)

        workbook = xlsxwriter.Workbook(file[0])
        worksheet = workbook.add_worksheet('Лист1')
        bold = workbook.add_format({'bold': True})
        for j in range(len(self.report_data[0])):
            worksheet.write(0, j, self.report_data[0][j], bold)

        ln = len(self.report_data[0])
        for i in range(1, len(self.report_data)):
            for j in range(ln):
                worksheet.write(i, j, self.report_data[i][j])
        workbook.close()
        self.pushButton_10.setEnabled(True)

    def closeEvent(self, event):
        self.create_dialog_1.close()
        self.create_dialog_2.close()
        event.accept()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    app.setStyleSheet(style_sheet)
    ex = MainApp()
    ex.show()
    sys.exit(app.exec())
