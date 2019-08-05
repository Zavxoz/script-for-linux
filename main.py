import argparse
from executors import HumanExecutor, InodeExecutor, BaseExecutor


def main():
    '''Command line utility which execute and parse df command'''
    parser = argparse.ArgumentParser()
    parser.add_argument("--human", action='store_true',
                        help="Display filesystems statistics\
                                   in human-readable format")
    parser.add_argument("--inode", action='store_true',
                        help="Getting information about inode's\
                                           in a filesystems")
    try:
        args = parser.parse_args()
        if args.human:
            result = HumanExecutor().execute()
        elif args.inode:
            result = InodeExecutor().execute()
        else:
            result = BaseExecutor().execute()
    except Exception as error:
        result = BaseExecutor().result(None, str(error), 1)
    finally:
        if result:
            print(result)
            with open("result.json", "w") as f:
                f.write(result)


if __name__ == "__main__":
    main()
