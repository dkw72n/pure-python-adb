__version__ = "0.1.7-dev"

class InstallError(Exception):
    def __init__(self, path, error):
        super(InstallError, self).__init__("{} could not be installed - [{}]".format(path, error))


class ClearError(Exception):
    def __init__(self, package, error):
        super(ClearError, self).__init__("Package {} could not be cleared - [{}]".format(package, error))

class FailError(Exception):
    pass

class PrematureEOFError(Exception):
    pass

class UnexpectedDataError(Exception):
    pass

class AdbConnectionError(Exception):
    pass