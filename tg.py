from py_tdlib import Client, Pointer
from py_tdlib.constructors import *
from Auth import Auth
from term import Term
import os

api_id = 717420
api_hash = "8446b305f854ca732ca78f83e0b2b0b7"

tdjson = Pointer(os.getcwd()+"/lib/libtdjson.so")
tdjson.verbosity(0)
client = Client(tdjson)

Auth(api_id, api_hash, client).phone()

result = client.send(getMe())
Term(client).prompt(result.first_name + result.last_name)

