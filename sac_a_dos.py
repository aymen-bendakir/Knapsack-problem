import sys
import random

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QWidget,
    QLabel,
    QDialog,
    QFormLayout,
    QVBoxLayout,
    QScrollArea,
    QPushButton,
    QHBoxLayout,
)


buttonCSS1 = """
    QPushButton {
        background-color: #4965CA; /* Blue */
        padding: 15px 32px;
        border-radius: 10%;
        color: white;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
    }
    
    QPushButton:hover {
        font-weight: bold;
        padding: 12px 28px;
    }
"""
buttonCSS2 = """
    QPushButton {
        background-color: #4CAF50; /* Green */
        padding: 20px 40px;
        border-radius: 10%;
        color: white;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 26px;
    }

    QPushButton:hover {
        font-weight: bold;
        padding: 12px 28px;
    }
"""
buttonCSS3 = """
    QPushButton {
        background-color: #4965CA; /* Blue */
        padding: 12px 28px;
        border-radius: 10%;
        color: white;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
    }

    QPushButton:hover {
        font-weight: bold;
        padding: 8px 22px;
    }
"""
buttonCSS4 = """
    QPushButton {
        background-color: #CF1010; /* Red */
        padding: 12px 28px;
        border-radius: 10%;
        color: white;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
    }

    QPushButton:hover {
        font-weight: bold;
        padding: 8px 22px;
    }
"""
tableRowCSS = """
    QWidget {
        background-color: #DBE3FF;
        border-radius: 15%;
    }
    
    QLineEdit {
        border-radius: 10%;
    }
"""
InputCSS = """
    background-color: #FFFFFF;
    border-radius: 10%;
"""
WrongInputCSS = """
    background-color: #FFDBDB;
    border-radius: 10%;
"""


class Window1(QDialog):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Sac a dos")
        self.generalLayout = QGridLayout()
        self.setLayout(self.generalLayout)
        self.setStyleSheet('background-color: #E9E9E9;')
        self.id = 1
        self._createDisplay()

    def _createDisplay(self):
        TitleMsg = QLabel("Problème du Sac à Dos", parent=self)
        TitleMsg.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        TitleMsg.setStyleSheet('font-size: 46px; font-weight: 700; margin-bottom: 20px')
        self.generalLayout.addWidget(TitleMsg, 0, 0, 1, 5)
        # right widget
        FormWidget = QWidget(parent=self)  # weight form
        FormWidget.setLayout(QFormLayout())
        Title1 = QLabel("Le poids maximal: ", parent=self)
        Title1.setStyleSheet('font-size: 20px; font-weight: 400;')
        self.weight = QLineEdit()
        self.weight.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.weight.setFixedHeight(Title1.height())
        self.weight.setFixedWidth(Title1.width())
        self.weight.setValidator(QIntValidator(1, 1000))
        self.weight.setStyleSheet(InputCSS)
        FormWidget.layout().addRow(Title1, self.weight)
        self.generalLayout.addWidget(FormWidget, 1, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

        RandomWidget = QWidget(parent=self)  # generate randomly form
        layout = QGridLayout(parent=self)
        RandomWidget.setLayout(layout)
        Title1 = QLabel("Générer aléatoirement ", parent=self)
        Title1.setStyleSheet('font-size: 20px; font-weight: 400;')
        layout.addWidget(Title1, 0, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        self.nbRandom = QLineEdit()
        self.nbRandom.setFixedHeight(Title1.height())
        self.nbRandom.setFixedWidth(Title1.width())
        self.nbRandom.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.nbRandom.setValidator(QIntValidator(1, 100))
        self.nbRandom.setStyleSheet(InputCSS)
        layout.addWidget(self.nbRandom, 0, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        Title1 = QLabel(" objets", parent=self)
        Title1.setStyleSheet('font-size: 20px; font-weight: 400;')
        layout.addWidget(Title1, 0, 2, alignment=Qt.AlignmentFlag.AlignCenter)
        GenerateButton = QPushButton("Générer")
        GenerateButton.clicked.connect(self._randomGenerate)
        GenerateButton.setStyleSheet(buttonCSS1)
        layout.addWidget(GenerateButton, 1, 0, 1, 3, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        self.generalLayout.addWidget(RandomWidget, 2, 0, 2, 2, alignment=Qt.AlignmentFlag.AlignCenter)

        ExecuteButton = QPushButton("Exécuter", parent=self)  # execute button
        ExecuteButton.clicked.connect(self._execute)
        ExecuteButton.setStyleSheet(buttonCSS2)
        self.generalLayout.addWidget(ExecuteButton, 4, 0, 1, 2, alignment=Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)

        # left widget
        ObjectsLayout = QVBoxLayout()
        self.generalLayout.addLayout(ObjectsLayout, 1, 2, 4, 3)

        Title2 = QLabel("Les objets", parent=self)
        Title2.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        Title2.setStyleSheet('font-size: 20px; font-weight: 400;')
        Title2.setFixedHeight(50)
        ObjectsLayout.addWidget(Title2)

        self.objectWin = QWidget(parent=self)  # table containing objects
        self.objectWin.setStyleSheet('background-color: #FFFFFF;')
        self.objectWin.setLayout(QVBoxLayout())
        self.objectWin.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
        scroll = QScrollArea(parent=self)  # scroll containing the table
        scroll.setWidget(self.objectWin)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scroll.setWidgetResizable(True)
        ObjectsLayout.addWidget(scroll)

        RowWidget = QWidget(parent=self.objectWin)  # first row: column names
        RowWidget.setStyleSheet('background-color: #4965CA; font-weight: 700; font-size: 14px; color: white; border-radius: 15%;')
        layout = QGridLayout()
        RowWidget.setLayout(layout)
        layout.addWidget(QLabel("ID", parent=RowWidget), 0, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(QLabel("Poids", parent=RowWidget), 0, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(QLabel("Valeur", parent=RowWidget), 0, 2, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(QLabel("Action", parent=RowWidget), 0, 3, alignment=Qt.AlignmentFlag.AlignCenter)
        RowWidget.setMaximumHeight(80)
        RowWidget.setMinimumHeight(80)
        self.objectWin.layout().addWidget(RowWidget)

        self._addInputRowObject()  # the add an object row

        self.generalLayout.addWidget(QWidget(), 5, 0, 1, 5)  # padding at the end of the screen

    def _addInputRowObject(self):
        self.AddRowInput = QWidget(parent=self.objectWin)
        self.AddRowInput.setStyleSheet(tableRowCSS)
        layout = QGridLayout()
        self.AddRowInput.setLayout(layout)
        self.idInput = QLabel(str(self.id), parent=self.AddRowInput)
        layout.addWidget(self.idInput, 0, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        self.weightInput = QLineEdit(parent=self.AddRowInput)
        self.weightInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.weightInput.setFixedSize(self.weight.size())
        self.weightInput.setStyleSheet('background-color: #FFFFFF;')
        self.weightInput.setValidator(QIntValidator(1, 1000))
        layout.addWidget(self.weightInput, 0, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        self.valueInput = QLineEdit(parent=self.AddRowInput)
        self.valueInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.valueInput.setFixedSize(self.weight.size())
        self.valueInput.setStyleSheet('background-color: #FFFFFF;')
        self.valueInput.setValidator(QIntValidator(1, 1000))
        layout.addWidget(self.valueInput, 0, 2, alignment=Qt.AlignmentFlag.AlignCenter)
        AddButton = QPushButton("Ajouter objet", parent=self.AddRowInput)
        AddButton.clicked.connect(self._addRowObject)
        AddButton.setStyleSheet(buttonCSS3)
        layout.addWidget(AddButton, 0, 3, alignment=Qt.AlignmentFlag.AlignCenter)
        self.AddRowInput.setMaximumHeight(80)
        self.AddRowInput.setMinimumHeight(80)
        self.objectWin.layout().addWidget(self.AddRowInput)

    def _addRowObject(self):
        try:
            self.valueInput.setStyleSheet(InputCSS)
            if not int(self.weightInput.text()):
                raise ValueError
        except ValueError:
            self.weightInput.setStyleSheet(WrongInputCSS)
            try:
                if not int(self.valueInput.text()):
                    raise ValueError
            except ValueError:
                self.valueInput.setStyleSheet(WrongInputCSS)
                return
            return
        try:
            self.weightInput.setStyleSheet(InputCSS)
            if not int(self.valueInput.text()):
                raise ValueError
        except ValueError:
            self.valueInput.setStyleSheet(WrongInputCSS)
            return
        self._addRow(self.idInput.text(), self.weightInput.text(), self.valueInput.text())

    def _addRow(self, id_, weight, value):
        self.objectWin.setStyleSheet('background-color: #FFFFFF;')
        self.id += 1
        self.objectWin.layout().removeWidget(self.AddRowInput)
        Row = QWidget(parent=self.objectWin)  # first row: column names
        Row.setStyleSheet(tableRowCSS)
        layout = QGridLayout()
        Row.setLayout(layout)
        layout.addWidget(QLabel(str(id_), parent=Row), 0, 0, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(QLabel(str(weight), parent=Row), 0, 1, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(QLabel(str(value), parent=Row), 0, 2, alignment=Qt.AlignmentFlag.AlignCenter)
        RemoveButton = QPushButton("Supprimer l'objet", parent=Row)
        RemoveButton.clicked.connect(self._removeRowObject)
        RemoveButton.setStyleSheet(buttonCSS4)
        layout.addWidget(RemoveButton, 0, 3, alignment=Qt.AlignmentFlag.AlignCenter)
        Row.setMaximumHeight(80)
        Row.setMinimumHeight(80)
        self.objectWin.layout().addWidget(Row)
        self.AddRowInput.adjustSize()
        self._addInputRowObject()

    def _removeRowObject(self):
        self.objectWin.layout().removeWidget(self.sender().parent())

    def _randomGenerate(self):
        try:
            if not int(self.nbRandom.text()):
                raise ValueError
        except ValueError:
            self.nbRandom.setStyleSheet(WrongInputCSS)
            return
        self.nbRandom.setStyleSheet(InputCSS)
        self.sender().setDisabled(True)
        for elem in self.objectWin.children()[2: len(self.objectWin.children()) - 1]:
            elem.children()[4].click()
        self.id = 1
        for _ in range(int(self.nbRandom.text())):
            self._addRow(self.id, random.randint(1, 50), random.randint(1, 50))
        self.sender().setDisabled(False)

    def _execute(self):
        try:
            int(self.weight.text())
            assert len(self.objectWin.children()) > 3
        except ValueError:
            self.weight.setStyleSheet(WrongInputCSS)
            try:
                assert len(self.objectWin.children()) > 3
            except AssertionError:
                self.objectWin.setStyleSheet('background-color: #FFDBDB;')
                return
            return
        except AssertionError:
            self.weight.setStyleSheet(InputCSS)
            self.objectWin.setStyleSheet('background-color: #FFDBDB;')
            return
        self.weight.setStyleSheet(InputCSS)
        weight = int(self.weight.text())  # total weight
        objects = {}  # dict(id: tuple(weight, value) )
        indexes = {}
        for i, elem in enumerate(self.objectWin.children()[2: len(self.objectWin.children()) - 1]):
            objects[i] = (int(elem.children()[2].text()), int(elem.children()[3].text()))
            indexes[i] = elem.children()[1].text()
        table = [[0] * (weight + 1) for _ in range(len(objects) + 1)]
        res = [[set()] * (weight + 1) for _ in range(len(objects) + 1)]
        for i in range(len(table)):
            for j in range(len(table[i])):
                if i == 0 or j == 0:
                    table[i][j] = 0
                elif j < objects[i - 1][0]:
                    table[i][j] = table[i - 1][j]
                    res[i][j] = res[i - 1][j]
                else:
                    if table[i - 1][j] <= table[i - 1][j - objects[i - 1][0]] + objects[i - 1][1]:
                        table[i][j] = table[i - 1][j - objects[i - 1][0]] + objects[i - 1][1]
                        res[i][j] = res[i - 1][j - objects[i - 1][0]].union({i - 1})
                    else:
                        table[i][j] = table[i - 1][j]
                        res[i][j] = res[i - 1][j]
        chosenObjects = [indexes[i] for i in res[-1][-1]]
        window2 = Window2(self, objects, indexes, table, chosenObjects)
        window2.showMaximized()


class Window2(QDialog):
    def __init__(self, window1_, objects, indexes, table, chosenObjects):
        super().__init__(parent=window1_)
        self.setWindowTitle("Resulats")
        self.generalLayout = QGridLayout()
        self.setLayout(self.generalLayout)
        self.setStyleSheet('background-color: #E9E9E9;')
        self._createDisplay(objects, indexes, table, chosenObjects)

    def _createDisplay(self, objects, indexes, table, chosenObjects):
        self.resultTable = QWidget(parent=self)  # table containing results
        self.resultTable.setStyleSheet('background-color: #FFFFFF;')
        self.resultTable.setLayout(QVBoxLayout())
        self.resultTable.layout().setAlignment(Qt.AlignmentFlag.AlignTop)
        scroll = QScrollArea(parent=self)  # scroll containing the table
        scroll.setWidget(self.resultTable)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        scroll.setWidgetResizable(True)
        self.generalLayout.addWidget(QWidget(), 0, 0, 1, 1)  # padding
        self.generalLayout.addWidget(scroll, 1, 1, 5, 7)
        self.generalLayout.addWidget(QWidget(), 6, 8, 1, 1)  # padding

        TitleMsg = QLabel(f"Les résultats", parent=self)
        TitleMsg.setAlignment(Qt.AlignmentFlag.AlignCenter)
        TitleMsg.setStyleSheet('font-size: 46px; font-weight: 700; margin-bottom: 20px')
        self.generalLayout.addWidget(TitleMsg, 0, 1, 1, 7)

        for i in range(len(table) + 1):
            RowWidget = QWidget(parent=self.resultTable)
            RowWidget.setLayout(QHBoxLayout())
            RowWidget.layout().setAlignment(Qt.AlignmentFlag.AlignLeft)
            for j in range(len(table[0]) + 1):
                if i == 0 and j == 0:
                    CellLabel = QLabel('Les poids\nLes objets', parent=RowWidget)
                elif i == 1 and j == 0:
                    CellLabel = QLabel("ID objet: 0\nPoids objet: 0\nValeur objet: 0", parent=RowWidget)
                elif i == 0:
                    CellLabel = QLabel(str(j - 1), parent=RowWidget)
                    CellLabel.setStyleSheet('background-color: #DBE3FF;')
                elif j == 0:
                    CellLabel = QLabel(f"ID objet: {indexes[i - 2]}\nPoids objet: {objects[i - 2][0]}\nValeur objet: {objects[i - 2][1]}", parent=RowWidget)
                    if indexes[i - 2] in chosenObjects:
                        CellLabel.setStyleSheet('background-color: #BDFFCC;')
                else:
                    CellLabel = QLabel(str(table[i - 1][j - 1]), parent=RowWidget)
                    if i == len(table) and j == len(table[0]):
                        CellLabel.setStyleSheet('background-color: #BDFFCC;')
                    elif i == 1 or j == 1:
                        CellLabel.setStyleSheet('background-color: #FFDBDB;')
                CellLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
                CellLabel.setFixedHeight(80)
                CellLabel.setFixedWidth(100)
                RowWidget.layout().addWidget(CellLabel)
            self.resultTable.layout().addWidget(RowWidget)

        TitleMsg = QLabel(f"Le gain maximal est: {table[-1][-1]}", parent=self)
        TitleMsg.setAlignment(Qt.AlignmentFlag.AlignCenter)
        TitleMsg.setStyleSheet('font-size: 46px; font-weight: 700; margin-bottom: 20px')
        self.generalLayout.addWidget(TitleMsg, 6, 1, 1, 7)


if __name__ == "__main__":
    app = QApplication([])
    window1 = Window1()
    window1.showMaximized()
    sys.exit(app.exec())
