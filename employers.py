import datetime as dt
import sqlite3

import xlrd
from PyQt5.QtWidgets import QDialog, QFileDialog

from employers_design import Ui_Dialog


class CreateNewEmployer(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_5.clicked.connect(self.addEmployer)
        self.pushButton_6.clicked.connect(self.addExcel)
        self.pushButton_7.clicked.connect(self.delEmployer)

    def addEmployer(self):
        c1 = self.lineEdit.text().strip().capitalize()  # Фамилия
        c2 = self.lineEdit_2.text().strip().capitalize()  # Имя
        c3 = self.lineEdit_3.text().strip().capitalize()  # Отчество
        c4 = self.lineEdit_4.text().strip().lower()  # Должность
        c5 = self.lineEdit_5.text().strip()  # Оклад
        c6 = self.lineEdit_6.text().strip()  # Коэф. Зн.
        c7 = self.dateEdit.text()
        c8 = self.textEdit_1.toPlainText()
        if c1 != '' and c2 != '' and c4 != '' and c5.isdigit() and c6.isdigit():
            try:
                con = sqlite3.connect('grades.db')
                cur = con.cursor()
                res = cur.execute("""SELECT * FROM employers WHERE surname = ? AND name = ? AND midname = ?""", (c1, c2, c3)).fetchall()
                if len(res) > 0:
                    cur.execute("""UPDATE employers SET position = ?, salary = ?, koef = ?, date = ?, extra = ? WHERE surname = ? AND name = ? AND midname = ?""", (c4, c5, c6, c7, c8, c1, c2, c3))
                    self.label_26.setText('Успешно обновлено!')
                else:
                    cur.execute("""INSERT INTO employers (surname, name, midname, position, salary, koef, date, extra) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", (c1, c2, c3, c4, c5, c6, c7, c8))
                    self.label_26.setText('Успешно добавлено!')
                con.commit()
                con.close()
                self.lineEdit.setText('') # Фамилия
                self.lineEdit_2.setText('')  # Имя
                self.lineEdit_3.setText('')  # Отчество
                self.lineEdit_4.setText('')  # Должность
                self.lineEdit_5.setText('')  # Оклад
                self.lineEdit_6.setText('')  # Коэф. Зн.
                self.textEdit_1.setText('')

            except Exception as e:
                self.label_26.setText('Ошибка!')
        else:
            self.label_26.setText('Необходимо корректно заполнить поля: ФИО, Должность, оклад, Коэф.Зн. ')


    def addExcel(self):
        try:
            self.file_name = QFileDialog.getOpenFileName(self, 'Выбор файла с данными о сотрудниках', "/Users/user_name/Desktop/","Excel(*.xlsx)")
            book = xlrd.open_workbook(self.file_name[0])
            sheet = book.sheet_by_index(0)
            num_rows = sheet.nrows
            num_col = sheet.ncols
            res = []
            base_date = dt.date(1900, 1, 1)
            for i in range(1, num_rows):
                s = []
                for j in range(num_col):
                    if j == 6:
                        birth = base_date + dt.timedelta(days=sheet.cell(i, j).value - 2)
                        s.append(birth.strftime("%d.%m.%Y"))
                    else:
                        s.append(sheet.cell(i, j).value)
                res.append(s)

            con = sqlite3.connect('grades.db')
            cur = con.cursor()

            for el in res:
                c1 = el[0].strip().capitalize()  # Фамилия
                c2 = el[1].strip().capitalize()  # Имя
                c3 = el[2].strip().capitalize()  # Отчество
                c4 = el[3].strip().lower()  # Должность
                c5 = el[4]  # Оклад
                c6 = el[5]  # Коэф. Зн.
                c7 = el[6]
                c8 = el[7].strip()
                if c1 != '' and c2 != '' and c3 != '' and c4 != '' and c5 and c6:
                    res = cur.execute("""SELECT * FROM employers WHERE surname = ? AND name = ? AND midname = ?""",
                                      (c1, c2, c3)).fetchall()
                    if len(res) > 0:
                        cur.execute(
                            """UPDATE employers SET position = ?, salary = ?, koef = ?, date = ?, extra = ? WHERE surname = ? AND name = ? AND midname = ?""",
                            (c4, c5, c6, c7, c8, c1, c2, c3,))
                    else:
                        cur.execute(
                            """INSERT INTO employers (surname, name, midname, position, salary, koef, date, extra) VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                            (c1, c2, c3, c4, c5, c6, c7, c8))
            con.commit()
            con.close()
            self.label_26.setText('Сотрудники успешно добавлены!')
        except Exception as e:
            self.label_26.setText('Ошибка загрузки .xlsx файла!')


    def delEmployer(self):
        c1 = self.lineEdit_7.text().strip().capitalize()  # Фамилия
        c2 = self.lineEdit_8.text().strip().capitalize()  # Имя
        c3 = self.lineEdit_9.text().strip().capitalize()  # Отчеств
        try:
            con = sqlite3.connect('grades.db')
            cur = con.cursor()
            cur.execute("""DELETE FROM employers WHERE surname = ? AND name = ? AND midname = ?""", (c1, c2, c3))
            con.commit()
            con.close()
            self.label_26.setText('Удалено успешно!')
            self.lineEdit_2.setText('')  # Имя
            self.lineEdit_3.setText('')  # Отчество
            self.lineEdit_4.setText('')
        except Exception as e:
            self.label_26.setText('Сотрудник не найден!')