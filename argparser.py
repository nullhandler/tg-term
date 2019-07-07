import argparse

def getArgs(argString):
    if argString.startswith("ls"):
        parser = argparse.ArgumentParser(description='')
        parser.add_argument("command")
        parser.add_argument("-n","--number", type=int,default=10, help='how many chats you want to display. (default: 10)')
        args = parser.parse_args(argString.split())
        return args
    elif argString.startswith("open"):
        parser = argparse.ArgumentParser(description='')
        parser.add_argument("command")
        parser.add_argument("-n","--number", type=int, help='which chat to open')
        parser.add_argument("-c","--count", type=int, help='number of messages')
        args = parser.parse_args(argString.split())
        return args
