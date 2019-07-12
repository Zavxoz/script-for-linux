class BaseExecutor(object):
    def __init__(self, cmd = 'df', *args):
        self.cmd = cmd
        self.args = args
        self.parser = BaseParser


    def command_maker(self):
        return command = list(df).extend([arg for arg in self.args])

class HumanExecutor(BaseExecutor):
    def __init__(self):
        super(HumanExecutor, self).__init__('df', '-h')
        self.parser = HumanParser


class InodeExecutor(BaseExecutor):
    def __init__():
        super(Inode_executor, self).__init__('df', '-i')
        self.parser = InodeParser