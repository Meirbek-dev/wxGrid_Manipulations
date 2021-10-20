#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint

import wx.xrc

from NewForm import MyFrame


class MyFrame(MyFrame):

    def fill(self, event):  # Метод заполнения таблицы случайными числами
        row = col = 0
        while row < self.table_array.GetNumberRows():  # Цикл по строкам
            while col < self.table_array.GetNumberCols():  # Цикл по колонам
                random_num = randint(0, 100)  # Присвоение переменной случайного значения от 0 до 100
                self.table_array.SetCellBackgroundColour(row, col, 'white')  # Изменение цвета ячейки на белый
                # Присвоение ячейке случайного значения из переменной random_num
                self.table_array.SetCellValue(row, col, "%d" % random_num)
                col += 1  # Переход на следующую колонку
            row += 1  # Переход на следующую строку
            col = 0  # Переход на первую колонку
        zero_counter = self.get_number_of_zeros()  # Присвоение переменной значения из метода нахождения нулей
        if not zero_counter:  # Код, выполняемый при отсутствии нулей
            # Установка текста в метках
            if self.m_toggleLang.GetValue():
                self.label_zero_counter.SetLabel('Number of zeros: 0')
                self.label_status.SetLabel('No zeros in the table!')
            else:
                self.label_zero_counter.SetLabel('Количество нулей: 0')
                self.label_status.SetLabel('В таблице нет нулей!')
        else:  # Код, выполняемый при наличии нулей
            if self.m_toggleLang.GetValue():
                self.label_zero_counter.SetLabel("Number of zeros: " + "%d" % zero_counter)
            else:
                self.label_zero_counter.SetLabel("Количество нулей: " + "%d" % zero_counter)
            self.label_status.SetLabel('')

    def execute(self, event):  # Метод выполнения задания
        row = col = 0
        zero_counter = self.get_number_of_zeros()
        try:
            if self.m_toggleLang.GetValue():
                self.label_status.SetLabel('Task completed!')
            else:
                self.label_status.SetLabel('Задание выполнено!')
            while row < self.table_array.GetNumberRows():
                while col < self.table_array.GetNumberCols():
                    number = int(self.table_array.GetCellValue(row, col))  # Присвоение переменной значения из ячейки
                    try:
                        if int(number) % 2 != 0:  # Проверка элемента ячейки на нечетность
                            # Присвоение ячейке значения равному количеству нулей в таблице и установка зеленого фона
                            str(self.table_array.SetCellValue(row, col, str(zero_counter)))
                            self.table_array.SetCellBackgroundColour(row, col, 'green')
                        elif int(number) % 2 == 0:  # Код, исполняемый если в ячейке четный элемент
                            self.table_array.SetCellBackgroundColour(row, col, 'cyan')
                    except Exception:
                        break
                    col += 1
                row += 1
                col = 0
            if self.m_toggleLang.GetValue():
                self.label_zero_counter.SetLabel("Number of zeros: " + "%d" % zero_counter)
            else:
                self.label_zero_counter.SetLabel("Количество нулей: " + "%d" % zero_counter)
        except Exception:  # Код, исполняемый в случае ошибки
            self.table_array.SetCellBackgroundColour(row, col, 'red')  # Установка ячейке красный цвет фона
            if self.m_toggleLang.GetValue():
                self.label_zero_counter.SetLabel('Only numbers are allowed!')
                self.label_status.SetLabel('Invalid data entered!')
            else:
                self.label_zero_counter.SetLabel('Можно вводить только числа!')
                self.label_status.SetLabel('Введены неверные данные!')

    def get_number_of_zeros(self):  # Метод получения количества нулей в таблице
        try:
            zero_counter = row = col = 0
            while row < self.table_array.GetNumberRows():
                while col < self.table_array.GetNumberCols():
                    number = int(self.table_array.GetCellValue(row, col))
                    # Если значение ячейки равно нулю, то прибавить единицу к счетчику нулей
                    if number == 0:
                        zero_counter += 1
                    col += 1
                row += 1
                col = 0
            return zero_counter  # Возврат значения количества нулей в таблице
        except Exception:
            return 0

    def toggle_lang(self, event):  # Методы смены языка приложения
        zero_counter = self.get_number_of_zeros()
        if self.m_toggleLang.GetValue():  # Проверка состояния кнопки переключения языка
            self.label_zero_counter.SetLabel('Number of zeros: ' + "%d" % zero_counter)
            self.label_status.SetLabel('Status')
            self.button_fill.SetLabel('Fill with random numbers')
            self.button_execute.SetLabel('Run task')
            self.label_task.SetLabel('Variant #1\nCount the number of zeros in the table and replace all odd\n'
                                     'integer elements of the table with this value.')
        else:
            self.label_zero_counter.SetLabel('Количество нулей: ' + "%d" % zero_counter)
            self.label_status.SetLabel('Статус')
            self.button_fill.SetLabel('Заполнить случайными числами')
            self.button_execute.SetLabel('Выполнить задание')
            self.label_task.SetLabel('Вариант №1\nПосчитать количество нулей в таблице и заменить все нечётные\n'
                                     'целые элементы таблицы на это значение.')


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None)
    frame.Show()
    app.MainLoop()
