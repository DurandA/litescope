from litescope.software.dump import *


class PythonDump(Dump):
    def __init__(self, dump=None):
        Dump.__init__(self)
        self.variables = [] if dump is None else dump.variables

    def generate_data(self):
        r = "dump = {\n"
        for variable in self.variables:
            r += "\"" + variable.name + "\""
            r += " : "
            r += str(variable.values)
            r += ",\n"
        r += "}"
        return r

    def write(self, filename):
        f = open(filename, "w")
        f.write(self.generate_data())
        f.close()

    def read(self, filename):
        raise NotImplementedError("Python files can not (yet) be read, please contribute!")
