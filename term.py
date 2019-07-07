from py_tdlib import Client
from argparser import getArgs
from chat import openChat
from py_tdlib.constructors import (
    getMe,
    getChats,
    getChat,
    chatTypePrivate,
    chatTypeBasicGroup,
    chatTypeSupergroup,
)


class Term():

    chatList = {}

    # Constructor
    def __init__(
        self,
        client: Client
    ): self.client = client

    # Terminal Prompt
    def prompt(self, username):
        while True:
            ip = input(username+"% ")
            if ip == "me":
                print(self.client.send(getMe()).first_name)
            elif ip == "help":
                print(
                    "\tme: prints your name\n\tls: gets your chats\n\topen: gets your msgs\n\tq: quits the client")
            elif ip == "q":
                self.client.stop()
                break
            else:
                args = getArgs(ip)
                if args.command == "ls":
                    result = self.client.send(
                        getChats(2 ** 63 - 1, 0, args.number))
                    i = 1
                    for chat_id in result.chat_ids:
                        user = self.client.send(getChat(chat_id))
                        self.chatList[i] = chat_id
                        if isinstance(user.type, chatTypePrivate):
                            print(str(i) + " " + user.title)
                        elif isinstance(user.type, chatTypeBasicGroup):
                            print(str(i) + " " + user.title + " (G)")
                        elif isinstance(user.type, chatTypeSupergroup):
                            if user.type.is_channel:
                                print(str(i) + " " + user.title + " (C)")
                            else:
                                print(str(i) + " " + user.title + " (G)")
                        i += 1
                elif args.command == "open":
                    openChat(self.client, self.chatList[args.number], args.count)
