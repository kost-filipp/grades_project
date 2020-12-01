import sqlite3

from PyQt5.QtWidgets import QDialog

from position_design import Ui_Dialog_1


class CreateNewPosition(QDialog, Ui_Dialog_1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_8.clicked.connect(self.addPosition)
        self.pushButton_9.clicked.connect(self.delPosition)

    def addPosition(self):
        c1 = self.lineEdit_10.text().strip().lower()  # Должность
        c2 = self.lineEdit_11.text().strip()  # Коэф
        c3 = self.lineEdit_12.text().strip()  # Зарплата
        c4 = self.lineEdit_13.text().strip().lower()  # Доп. инфо.
        if c1 != '' and c2.isdigit() and c3.isdigit():
            try:
                con = sqlite3.connect('grades.db')
                cur = con.cursor()
                res = cur.execute("""SELECT * FROM positions WHERE position = ?""", (c1,)).fetchall()
                if len(res) > 0:
                    cur.execute("""UPDATE positions SET koef = ?, salary = ?, extra = ? WHERE position = ?""",
                                (c2, c3, c4, c1))
                    self.label_35.setText('Успешно обновлено!')
                else:
                    cur.execute("""INSERT INTO positions (position, koef, salary, extra) VALUES (?, ?, ?, ?)""", (c1, c2, c3, c4))
                    self.label_35.setText('Успешно добавлено!')
                con.commit()
                con.close()
                self.lineEdit_10.setText('')
                self.lineEdit_11.setText('')
                self.lineEdit_12.setText('')
                self.lineEdit_13.setText('')

            except Exception as e:
                self.label_35.setText('Ошибка!')
        else:
            self.label_35.setText('Необходимо корректно заполнить поля!')


    def delPosition(self):
        c1 = self.lineEdit_14.text().strip().lower()  # Должность
        try:
            con = sqlite3.connect('grades.db')
            cur = con.cursor()
            res = cur.execute("""SELECT * FROM positions WHERE position = ?""", (c1,)).fetchall()
            if len(res) > 0:
                cur.execute("""DELETE FROM positions WHERE position = ?""", (c1,))
                con.commit()
                con.close()
                self.label_35.setText('Удалено успешно!')
                self.lineEdit_14.setText('')
            else:
                self.label_35.setText('Должность не найдена!')
        except Exception as e:
            self.label_35.setText('Ошибка!')