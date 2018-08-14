# Module for working with project's database
import win32com.client


class DataBase:
    def __init__(self, path):
        self.path = path
        self.connection = win32com.client.Dispatch('ADODB.Connection')
        self.cmd = win32com.client.Dispatch('ADODB.Command')

    def open(self):
        path = self.path + '\\Data'
        dsn = 'Provider=VFPOLEDB.1;Data Source={}'.format(path)
        self.connection.Open(dsn)

    def read(self):
        self.cmd.ActiveConnection = self._connection
#        cmd.CommandText = "SELECT name, algname, usotype FROM tbDigOutParam;"
        self.cmd.CommandText = "SELECT * FROM tbUSOType;"

        rs, total = self.cmd.Execute()

        while total:
            for x in range(rs.Fields.Count):
                print('{} --> {}'.format(rs.Fields.item(x).Name,
                                         rs.Fields.item(x).Value))
            rs.MoveNext()
            total = total - 1
            print('=' * 80)
