#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from random import randint

import wx.xrc

from NewForm import MyFrame


class MyFrame(MyFrame):

    def fill(self, event):
        row = col = 0
        while row < self.table_array.GetNumberRows():
            while col < self.table_array.GetNumberCols():
                random_num = randint(0, 100)
                self.table_array.SetCellBackgroundColour(row, col, 'white')
                self.table_array.SetCellValue(row, col, "%d" % random_num)
                col += 1
            row += 1
            col = 0
        zero_counter = self.get_number_of_zeros()
        if not zero_counter:
            self.label_zero_counter.SetLabel('Number of zeros: 0')
            self.label_status.SetLabel('No zeros in the table!')
        else:
            self.label_zero_counter.SetLabel("Number of zeros: " + "%d" % zero_counter)
            self.label_status.SetLabel('')

    def execute(self, event):
        row = col = 0
        zero_counter = self.get_number_of_zeros()
        try:
            self.label_status.SetLabel('Task completed!')
            while row < self.table_array.GetNumberRows():
                while col < self.table_array.GetNumberCols():
                    number = int(self.table_array.GetCellValue(row, col))
                    try:
                        if int(number) % 2 != 0:
                            str(self.table_array.SetCellValue(row, col, str(zero_counter)))
                            self.table_array.SetCellBackgroundColour(row, col, 'green')
                        elif int(number) % 2 == 0:
                            self.table_array.SetCellBackgroundColour(row, col, 'cyan')
                    except Exception:
                        break
                    col += 1
                row += 1
                col = 0
            self.label_zero_counter.SetLabel("Number of zeros: " + "%d" % zero_counter)
        except Exception:
            self.table_array.SetCellBackgroundColour(row, col, 'red')
            self.label_zero_counter.SetLabel('Only numbers are allowed!')
            self.label_status.SetLabel('Invalid data entered!!')

    def get_number_of_zeros(self):
        try:
            zero_counter = row = col = 0
            while row < self.table_array.GetNumberRows():
                while col < self.table_array.GetNumberCols():
                    number = int(self.table_array.GetCellValue(row, col))
                    if number == 0:
                        zero_counter += 1
                    col += 1
                row += 1
                col = 0
            return zero_counter
        except Exception:
            return 0

    def OnCloseFrame(self, event):
        self.Destroy()


if __name__ == '__main__':
    app = wx.App()
    frame = MyFrame(None)
    frame.Show()
    app.MainLoop()
