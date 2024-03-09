import PyQt6.QtWidgets as qt
import PyQt6.QtGui as qt1
import PyQt6.QtCore as qt2
class Azkar(qt.QDialog):
    def __init__(self,p,text):
        super().__init__()
        self.text=text
        self.setWindowTitle(_("azkar"))
        self.showFullScreen()
        self.index=0
        self.azkarText=qt.QLineEdit(text[0]["zekr"])
        self.info=qt.QLineEdit(text[0]["bless"])
        self.azkarText.setReadOnly(True)
        self.info.setReadOnly(True)
        self.repeat=qt.QSpinBox()
        self.repeat.setReadOnly(True)
        self.repeat.setRange(1,1000)
        self.repeat.setValue(text[0]["repeat"])
        self.next=qt.QPushButton(_("next"))
        self.next.clicked.connect(self.on_next)
        layout=qt.QFormLayout(self)
        layout.addRow(_("zekr"),self.azkarText)
        layout.addRow(_("information"),self.info)
        layout.addRow(_("repeat"),self.repeat)
        layout.addWidget(self.next)
    def on_next(self):
        if self.index==len(self.text)-1:
            qt.QMessageBox.information(self,_("done"),_("you read all azkar successfuly"))
            self.close()
        else:
            self.index+=1
            t=self.text[self.index]
            self.azkarText.setText(t["zekr"])
            self.info.setText(t["bless"])
            self.repeat.setValue(t["repeat"])
            self.azkarText.setFocus()