from database import DataBase
import code

# from PyQt5.QtWidgets import QApplication, QDialog


# app = QApplication(sys.argv)
# window = QDialog()


# window.show()
# sys.exit(app.exec_())

db = DataBase("D:\py\Database")
db.open()
db.read()
db.close()

#code.create(abonent.dgo)
