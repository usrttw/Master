import unittest
from PyQt5.QtWidgets import QApplication
from intro import material


class TestMaterialCalculation(unittest.TestCase):

    def test_material_calculation(self):
        # Создаем объект приложения QtWidgets.QApplication
        app = QApplication([])

        # Создаем объект material для тестирования
        widget = material()

        # Устанавливаем значения для comboBox и comboBox_2
        widget.comboBox.addItem("Product A")
        widget.comboBox_2.addItem("Material A")

        # Устанавливаем значение в поле ввода
        widget.lineEdit.setText("10")

        # Запускаем функцию подсчета
        widget.sum()

        # Получаем текст из label_3
        result = widget.label_3.text()

        # Проверяем, что результат соответствует ожидаемому
        self.assertEqual(result, "Для такого количества Product A нужно 11 Material A")

        # Закрываем приложение
        app.exit()


if __name__ == '__main__':
    unittest.main()
