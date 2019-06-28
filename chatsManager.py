from py_tdlib.constructors import getChatHistory

def getMyMessages(client, id, limit):
    from_id = 0
    msgs = []
    tmp = True
    while tmp:
        result = client.send(getChatHistory(id,from_id,0,limit,False))
        msgs.extend(result.messages)
        #print(len(msgs))
        if result.total_count != 0:
            from_id = result.messages[-1].id
        if len(msgs) > limit:
            tmp = False
    return msgs