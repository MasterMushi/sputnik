# Classes for working with project's database


class Abonent:

    def __init__(self, symbname):
        self.symbname = symbname
        self.dgo = []

    class Dgo:
        def __init__(self, symbname, algname):
            self.symbname = symbname
            self.algname = algname

    def dgo_add(self, symbname, algname):
        _dgo = self.Dgo(symbname, algname)
        self.dgo.append(_dgo)
