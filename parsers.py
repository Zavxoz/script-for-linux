import re


class BaseParser(object):
    def __init__(self, string):
        self.string = string
        self. output_dict = {}
        self.keys_for_dict = ['Filesystem', '1K-blocks', 'Used',
                            'Available', 'Use%', 'Mounted on']
        self.template = (r'(?P<first>\S+)\s*(?P<second>\d+)\s*'
                         r'(?P<third>\d+)\s*(?P<fourth>\d+)\s*'
                         r'(?P<fifth>\d+[%])\s*(?P<sixth>\S+)')


    def make_dict_from_string(self):
        pattern = re.compile(self.template)
        matched_data = re.findall(pattern, self.string.decode("utf-8"))
        for single_match in matched_data:
            inserted_dict = {}
            i = 0
            for name in self.keys_for_dict:
                inserted_dict[name] = single_match[i]
                i += 1
            filesystem_name = "Filesystem '{}' mounted on '{}'".\
                format(single_match[0], single_match[-1])
            self.output_dict[filesystem_name] = inserted_dict
        return self.output_dict

class HumanParser(BaseParser):
    def __init__(self, string):
        super(HumanParser, self).__init__(string)
        self.string = string
        self.keys_for_dict = ['Filesystem', 'Size', 'Used',
                            'Avail', 'Use%', 'Mounted on']
        self.template = (r'(?P<first>\S+)\s*(?P<second>\S+)\s*'
                            r'(?P<third>\S+)\s*(?P<fourth>\S+)\s*'
                            r'(?P<fifth>\d+[%])\s*(?P<sixth>\S+)')

class InodeParser(BaseParser):
    def __init__(self, string):
        super(InodeParser, self).__init__(string)
        self.string = string
        self.keys_for_dict = ['Filesystem', 'Inodes', 'IUsed',
                            'IFree', 'IUse%', 'Mounted on']
