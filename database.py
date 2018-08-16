# Module for working with project's database
import win32com.client


class DataBase:
    def __init__(self, path):
        self.path = path + '\Data'
        self.connection = win32com.client.Dispatch('ADODB.Connection')
        self.cmd = win32com.client.Dispatch('ADODB.Command')
        self.dsn = 'Provider=VFPOLEDB.1;Data Source={}'.format(self.path)

    def open(self):
        self.connection.Open(self.dsn)

    def close(self):
        self.connection.Close()

    def read(self):
        self.cmd.ActiveConnection = self.connection
        self.cmd.CommandText = "SELECT * FROM tbDigOutParam;"
#        self.cmd.CommandText = "SELECT * FROM tbUSOType;"

        rs, total = self.cmd.Execute()
        print(rs)
        while total:
            for x in range(rs.Fields.Count):
                print('{} --> {}'.format(rs.Fields.item(x).Name,
                                         rs.Fields.item(x).Value))
            rs.MoveNext()
            total = total - 1
            print('=' * 80)
