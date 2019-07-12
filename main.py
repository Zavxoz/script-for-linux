from subprocess import Popen, PIPE
import json
import argparse

class F(argparse.Action):
    def __init__(self,option_strings,
                 dest=None,
                 nargs=0,
                 default=None,
                 required=False,
                 type=None,
                 metavar=None,
                 help=None):
        super(F, self).__init__(
            option_strings=option_strings,
            dest=dest,
            nargs=nargs,
            default=default,
            required=required,
            metavar=metavar,
            type=type,
            help=help)

    def __call__(self, parser, namespace, values, option_string=None):
        with Popen(["df", "-h"], stdout = PIPE) as proc:          
            data = proc.stdout.read().decode("utf-8") 

class F1(argparse.Action):
    def __init__(self,option_strings,
                 dest=None,
                 nargs=0,
                 default=None,
                 required=False,
                 type=None,
                 metavar=None,
                 help=None):
        super(F1, self).__init__(
            option_strings=option_strings,
            dest=dest,
            nargs=nargs,
            default=default,
            required=required,
            metavar=metavar,
            type=type,
            help=help)
    def __call__(self, parser, namespace, values, option_string=None):
        with Popen(["df", "-i"]) as proc:
            data = proc.stdout.read().decode("utf-8")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--human", action = F, help = "Execute and parse linux system command “df -h”")
    parser.add_argument("--inode", action = F1, help = "Execute and parse linux system command “df -i”")
    results = parser.parse_args()


if __name__ == "__main__":
    main()