import threading
import os, sys
from chatsManager import getMyMessages
from py_tdlib.constructors import (
    updateNewMessage,
    messageText,
    getMe,
    getUser
)
from colorama import Fore

# Async Method to get incoming messages
def getRealUpdates(client):
    for update in client.get_updates():
        if isinstance(update,updateNewMessage):
            print(update.message.content.text.text)

def openChat(client, id, limit):
    os.system('cls' if os.name == 'nt' else 'clear')
    user = client.send(getMe())
    fromUser = client.send(getUser(id))
    # Start the async method in another thread
    #threading.Thread(target=getRealUpdates,args=(client,)).start()
    result = getMyMessages(client,id,limit)
    result.reverse()
    for message in result:
        if isinstance(message.content, messageText):
            if message.sender_user_id == user.id:
                print(user.first_name + user.last_name ,end=": ")
            else:
                print(fromUser.first_name + fromUser.last_name, end=': ')
            print(message.content.text.text)
    exit = False
    while (exit != True):
        ip = input("msg: ")
        if ip == 'q':
            exit = True
        else:
            # One hell of a hack
            print("\033[A                             \033[A")
            print(ip)