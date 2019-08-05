from subprocess import Popen, PIPE
from parsers import BaseParser, HumanParser, InodeParser
import json


class BaseExecutor(object):
    '''class to make a command'''
    def __init__(self, cmd='df', *args):
        self.cmd = cmd
        self.args = args
        self.parser = BaseParser

    def command_maker(self):
    '''make command from arguments'''
        tmp = []
        tmp.append(self.cmd)
        tmp.extend([arg for arg in self.args])
        return tmp

    def execute(self):
    '''execute command in shell'''
        with Popen(self.command_maker(), stdout=PIPE, stderr=PIPE) as proc:
            data, error = proc.communicate()
            return_code = proc.returncode
            if return_code == 0:
                result_dict = self.parser(data.decode(
                    "utf-8")).make_dict_from_string()
                return self.result(result_dict, str(error.decode("utf-8")),
                                   return_code)
            else:
                return self.result(None, str(error.decode("utf-8")),
                                   return_code)

    def result(self, result_dict, error, return_code):
        """Serialize output to a json format"""
        if return_code:
            status = 'failure'
        else:
            status = 'success'
        as_dict = {
            'status': status,
            'error': error,
            'result': result_dict
        }
        json_data = json.dumps(as_dict, sort_keys=False,
                               indent=4, separators=(',', ': '))
        return json_data


class HumanExecutor(BaseExecutor):
    '''class to execute command with argument -h'''
    def __init__(self):
        super(HumanExecutor, self).__init__('df', '-h')
        self.parser = HumanParser


class InodeExecutor(BaseExecutor):
    '''class to execute command with argument -i'''
    def __init__(self):
        super(InodeExecutor, self).__init__('df', '-i')
        self.parser = InodeParser
