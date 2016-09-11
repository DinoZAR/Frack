
class Program(object):

    def __init__(self):
        self.functions = []

class Function(object):

    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters

class Parameter(object):

    def __init__(self, name, dataType):
        self.name = name
        self.dataType = dataType