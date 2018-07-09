import database
import code

# from PyQt5.QtWidgets import QApplication, QDialog


# app = QApplication(sys.argv)
# window = QDialog()


# window.show()
# sys.exit(app.exec_())

abonent = database.Abonent('ЗРУ')
abonent.dgo_add('Наименование 1', 'alg_name1')
abonent.dgo_add('Наименование 2', 'alg_name2')

code.create(abonent.dgo)
