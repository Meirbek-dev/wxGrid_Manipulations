# -*- coding: utf-8 -*-

###########################################################################
# Python code generated with wxFormBuilder (version Oct 26 2018)
# http://www.wxformbuilder.org/
##
# PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.grid
import wx.xrc


###########################################################################
# Class MyFrame
###########################################################################

class MyFrame(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Table-Array on wxPython", pos=wx.DefaultPosition,
                          size=wx.Size(544, 269), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL,
                          name=u"Table-Array on WxPython")
        self.SetSizeHints(wx.Size(544, 269), wx.Size(544, 269))
        self.SetIcon(wx.Icon("logo.png"))
        style = self.GetWindowStyle()
        self.SetWindowStyle(style & (~wx.CLOSE_BOX) & (~wx.MAXIMIZE_BOX))
        self.SetFont(wx.Font(12, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Courier New"))

        gbSizer = wx.GridBagSizer(0, 0)
        gbSizer.SetFlexibleDirection(wx.BOTH)
        gbSizer.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.table_array = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.table_array.CreateGrid(4, 5)
        self.table_array.EnableEditing(True)
        self.table_array.EnableGridLines(True)
        self.table_array.EnableDragGridSize(False)
        self.table_array.SetMargins(0, 0)

        # Columns
        self.table_array.SetColSize(0, 50)
        self.table_array.SetColSize(1, 50)
        self.table_array.SetColSize(2, 50)
        self.table_array.SetColSize(3, 50)
        self.table_array.SetColSize(4, 50)
        self.table_array.EnableDragColMove(False)
        self.table_array.EnableDragColSize(False)
        self.table_array.SetColLabelSize(30)
        self.table_array.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.table_array.AutoSizeRows()
        self.table_array.EnableDragRowSize(False)
        self.table_array.SetRowLabelSize(30)
        self.table_array.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.table_array.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        gbSizer.Add(self.table_array, wx.GBPosition(0, 0), wx.GBSpan(3, 1), wx.ALL, 5)

        self.button_fill = wx.Button(self, wx.ID_ANY, u"Fill with random numbers", wx.DefaultPosition, wx.Size(230, -1),
                                     0)
        self.button_fill.SetFont(
            wx.Font(10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Courier New"))
        self.button_fill.SetMaxSize(wx.Size(230, -1))

        gbSizer.Add(self.button_fill, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.ALIGN_CENTER | wx.ALL, 5)

        self.button_execute = wx.Button(self, wx.ID_ANY, u"Run task", wx.DefaultPosition, wx.Size(230, -1), 0)
        self.button_execute.SetFont(
            wx.Font(10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Courier New"))
        self.button_execute.SetMaxSize(wx.Size(500, -1))

        gbSizer.Add(self.button_execute, wx.GBPosition(1, 1), wx.GBSpan(1, 1), wx.ALIGN_CENTER | wx.ALL, 5)

        self.label_zero_counter = wx.StaticText(self, wx.ID_ANY, u"Number of zeros:", wx.DefaultPosition,
                                                wx.DefaultSize, 0)
        self.label_zero_counter.Wrap(-1)

        self.label_zero_counter.SetFont(
            wx.Font(10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Courier New"))

        gbSizer.Add(self.label_zero_counter, wx.GBPosition(3, 0), wx.GBSpan(3, 1), wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

        self.label_task = wx.StaticText(self, wx.ID_ANY,
                                        u"Variant #1\nCount the number of zeros in the table and replace all "
                                        u"odd\ninteger elements of the table with this value.",
                                        wx.DefaultPosition, wx.DefaultSize, 0)
        self.label_task.Wrap(-1)

        self.label_task.SetFont(
            wx.Font(10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Courier New"))

        gbSizer.Add(self.label_task, wx.GBPosition(6, 0), wx.GBSpan(1, 2), wx.ALL | wx.EXPAND, 5)

        self.label_status = wx.StaticText(self, wx.ID_ANY, u"Status", wx.DefaultPosition, wx.DefaultSize, 0)
        self.label_status.Wrap(-1)

        self.label_status.SetFont(
            wx.Font(10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Courier New"))

        gbSizer.Add(self.label_status, wx.GBPosition(3, 1), wx.GBSpan(3, 1),
                    wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.TOP, 5)

        self.m_toggleLang = wx.ToggleButton(self, wx.ID_ANY, u"Russian/English", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_toggleLang.SetValue(True)
        self.m_toggleLang.SetFont(
            wx.Font(10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Courier New"))

        gbSizer.Add(self.m_toggleLang, wx.GBPosition(2, 1), wx.GBSpan(1, 1), wx.ALIGN_CENTER | wx.ALL, 5)

        self.SetSizer(gbSizer)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.button_fill.Bind(wx.EVT_BUTTON, self.fill)
        self.button_execute.Bind(wx.EVT_BUTTON, self.execute)
        self.m_toggleLang.Bind(wx.EVT_TOGGLEBUTTON, self.toggle_lang)

    def __del__(self):
        pass
