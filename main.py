from subprocess import Popen, PIPE
import json
import argparse
import re
from executors import HumanExecutor, InodeExecutor, BaseExecutor
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--human", action = 'store', 
                                    help = "Display filesystems statistics in human-readable format")
    parser.add_argument("--inode", action = 'store', 
                                    help = "Getting information about inode's in a filesystems")
    try:
        args = parser.parse_args()
        if args.human:
            result = HumanExecutor.execute()  
        elif args.inode:
            result = InodeExecutor.execute()
        else:
            result = BaseExecutor().execute()
    except Exception as error: pass
    finally :pass


if __name__ == "__main__":
    main()
