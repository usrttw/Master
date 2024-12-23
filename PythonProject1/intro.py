from PyQt5 import QtWidgets
import pymysql
import sys
from untitled import Ui_MainWindow
import untitled_1
import untitled_2
import untitled_3
import untitled_4

database = pymysql.connect(host='127.0.0.1', user='root',
                           password='root', database='MP')


class Osnova(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self)
        self.ad = None
        self.parent = parent
        self.current_text = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.Avtorizacia_and_perehod)

    def Avtorizacia_and_perehod(self):
        login = self.ui.lineEdit.text()
        password = self.ui.lineEdit_2.text()
        cursor = database.cursor()
        try:
            if login == '' or password == '':
                QtWidgets.QMessageBox.warning(self, "Ошибка", "Заполните поля логина и пароля.")
            else:
                query_A = "SELECT * FROM polzovateli WHERE login = %s AND password = %s"
                cursor.execute(query_A, (login, password))
                result = cursor.fetchone()
                if result:
                    print("Authorization was successful")
                    self.ad = glavnoe()
                    self.ad.show()
                    self.hide()
                else:
                    QtWidgets.QMessageBox.warning(self, "Ошибка", "Неверный логин или пароль.")
        except pymysql.Error as e:
            QtWidgets.QMessageBox.critical(self, "Ошибка", f"Ошибка базы данных: {e}")
        finally:
            cursor.close()


class glavnoe(QtWidgets.QMainWindow, untitled_1.Ui_MainWindow):
    def __init__(self):
        super(glavnoe, self).__init__()
        self.ad = None
        self.setupUi(self)

        self.pushButton.clicked.connect(self.perexod)
        self.pushButton_2.clicked.connect(self.vibor)
        print('Dva')

    def vibor(self):
        cursor = database.cursor()
        P = self.comboBox.currentText()
        print(P)
        if P == "":
            self.lineEdit.setText("Выберите услугу")
        elif P == "Добавить поставщика":
            self.ad = dobavlenie()
            self.ad.show()
            self.hide()
        elif P == "удалить поставщика":
            self.ad = ydalenie()
            self.ad.show()
            self.hide()

    def perexod(self):
        self.ad = material()
        self.ad.show()
        self.hide()

class dobavlenie(QtWidgets.QMainWindow, untitled_2.Ui_MainWindow):
    def __init__(self):
        super(dobavlenie, self).__init__()
        self.setupUi(self)

        cursor = database.cursor()

        self.pushButton.clicked.connect(self.vixod)
        self.pushButton_2.clicked.connect(self.save_and_vixod)

    def vixod(self):
        self.ad = glavnoe()
        self.ad.show()
        self.hide()

    def save_and_vixod(self):
        type_ = self.lineEdit.text()
        phone = self.lineEdit_2.text()
        name = self.lineEdit_3.text()
        director = self.lineEdit_4.text()
        inn = self.lineEdit_5.text()
        email = self.lineEdit_6.text()
        rating = self.lineEdit_7.text()

        if not type_ or not phone or not name:
            QtWidgets.QMessageBox.warning(self, "Ошибка",
                                          "Поля 'Тип', 'Телефон' и 'Наименование' обязательны для заполнения.")
            return

        cursor = database.cursor()
        try:
            query_insert = """
              INSERT INTO postavshiki (Partner_type, Partners_phone_number, Partners_phone_number, Director, TIN, Partner_email, Rating)
              VALUES (%s, %s, %s, %s, %s, %s, %s)
          """
            cursor.execute(query_insert, (type_, phone, name, director, inn, email, rating))
            database.commit()
            QtWidgets.QMessageBox.information(self, "Успех", "Данные поставщика успешно добавлены.")
        except pymysql.Error as e:
            QtWidgets.QMessageBox.critical(self, "Ошибка", f"Ошибка базы данных: {e}")
        finally:
            cursor.close()

class ydalenie(QtWidgets.QMainWindow, untitled_3.Ui_MainWindow):
    def __init__(self):
        super(ydalenie, self).__init__()
        self.setupUi(self)
        cursor = database.cursor()

        cursor.execute(f'SELECT Partners_phone_number FROM partners_import')
        x = cursor.fetchall()
        for r in x:
            self.comboBox.addItem(r[0])


        self.pushButton_2.clicked.connect(self.vixod_2)
        self.pushButton.clicked.connect(self.save_and_vixod_2)

    def vixod_2(self):
        self.ad = glavnoe()
        self.ad.show()
        self.hide()

    def save_and_vixod_2(self):
        selected_phone = self.comboBox.currentText()

        if not selected_phone:
            QtWidgets.QMessageBox.warning(self, "Ошибка", "Пожалуйста, выберите поставщика из списка.")
            return

        cursor = database.cursor()
        try:
            query_delete = "DELETE FROM partners_import WHERE Partners_phone_number = %s"
            cursor.execute(query_delete, (selected_phone,))
            if cursor.rowcount > 0:
                database.commit()
                QtWidgets.QMessageBox.information(self, "Успех", "Поставщик успешно удален.")
                self.load_phone_numbers()  # Update the list after deletion
            else:
                QtWidgets.QMessageBox.warning(self, "Внимание", "Поставщик с таким телефоном не найден.")
        except pymysql.Error as e:
            QtWidgets.QMessageBox.critical(self, "Ошибка", f"Ошибка базы данных: {e}")
        finally:
            cursor.close()


class material(QtWidgets.QMainWindow,untitled_4.Ui_MainWindow):
    def __init__(self,):
        super(material,self).__init__()
        self.ad = None
        self.setupUi(self)

        self.pushButton_2.clicked.connect(self.vixod_4)
        self.pushButton.clicked.connect(self.sum)

        cursor = database.cursor()
        try:
            cursor.execute(f'SELECT Product_type FROM product_type_import')
            q = cursor.fetchall()
            for r in q:
                self.comboBox.addItem(r[0])

            cursor.execute(f'SELECT Material_type FROM material_type_import')
            q = cursor.fetchall()
            for r in q:
                self.comboBox_2.addItem(r[0])
        except pymysql.Error as e:
            print("Ошибка базы данных:", e)
        finally:
            cursor.close()

    def sum(self):
        cursor = database.cursor()
        try:
            sum1 = self.comboBox.currentText()
            sum2 = self.comboBox_2.currentText()
            summa = self.lineEdit.text()
            cursor.execute(f'SELECT Product_Type_Factor FROM product_type_import WHERE Product_type = "{sum1}"')
            t1 = cursor.fetchall()
            cursor.execute(f'SELECT Material_scrap_percentage FROM material_type_import WHERE Material_type = "{sum2}"')
            t2 = cursor.fetchall()
            pert = int(summa) * t1[0][0] / (1 - (t2[0][0] / 100))
            q, r = divmod(pert, 1)
            y = round(q) + bool(r)
            self.label_3.setText("Для такого количества " '\n' + sum1 + " нужно " + str(y) + " " + sum2)
        except pymysql.Error as e:
            print("Ошибка базы данных:", e)
        finally:
            cursor.close()

    def vixod_4(self):
        self.ad = glavnoe()
        self.ad.show()
        self.hide()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = Osnova()
    myapp.show()
    sys.exit(app.exec())

database.close()