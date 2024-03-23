# write a code for the second app
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QApplication , QWidget, QLabel, 
    QPushButton , QVBoxLayout , QHBoxLayout,
    QLineEdit)

from instr import*

class TestWin (QWidget):
    def __init__(self):
        super().__init__()
        self.set_appear()
        self.initUI()
        self.connects()
        self.show()
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)
    def initUI(self):
        self.h_line=QHBoxLayout()
        self.r_line=QVBoxLayout()
        self.l_line=QVBoxLayout()

        self.text_name=QLabel(txt_name)
        self.text_age=QLabel(txt_age)
        self.text_test1=QLabel(txt_test1)
        self.text_test2=QLabel(txt_test2)
        self.text_test3=QLabel(txt_test3)
        self.text_timer=QLabel(txt_timer)
        
        self.btn_next=QPushButton(txt_sendresults)
        self.btn_test1=QPushButton(txt_starttest1)
        self.btn_test2=QPushButton(txt_starttest2)
        self.btn_test3=QPushButton(txt_starttest3)
        
        self.line_name=QLineEdit(txt_hintname)
        self.line_age=QLineEdit(txt_hintage)
        self.line_test1=QLineEdit(txt_hinttest1)
        self.line_test2=QLineEdit(txt_hinttest2)
        self.line_test3=QLineEdit(txt_hinttest3)
        
        self.r_line.addWidget(self.text_timer, alignment = Qt.AlignCenter)
        self.l_line.addWidget(self.text_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_name, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_age, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test1, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.text_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test2, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.line_test3, alignment = Qt.AlignLeft)
        self.l_line.addWidget(self.btn_next, alignment = Qt.AlignCenter)

        self.h_line.addLayout(self.l_line)
        self.h_line.addLayout(self.r_line)
        self.setLayout(self.h_line)

    def next_click(self):
       self.hide()
       self.fw = FinalWin()


    def connects(self):
       self.btn_next.clicked.connect(self.next_click)

