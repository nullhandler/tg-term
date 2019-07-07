from py_tdlib.constructors import getChatHistory

def getMyMessages(client, id, limit):
    count = 0
    from_id = 0
    msgs = []
    tmp = True
    while tmp:
        count = count + 1
        if count == 500:
            print("Nobody wants to load 500 messages")
        result = client.send(getChatHistory(id,from_id,0,limit,False))
        msgs.extend(result.messages)
        #print(len(msgs))
        if result.total_count != 0:
            from_id = result.messages[-1].id
        if len(msgs) > limit:
            tmp = False
    #print(msgs)
    return msgs