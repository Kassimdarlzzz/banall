# Powred By Bikash Gadgets Tech 
# Owner Of Bgt BikashHalder
# Bikash Bro Aditya Halder

import os

class Config:
    BOT_TOKEN=os.environ['BOT_TOKEN']
    SUDO=os.environ['SUDO']
    OWNER=os.environ['OWNER']
    API_HASH=os.environ['API_HASH']
    API_ID=int(os.environ['API_ID'])
    
    if not BOT_TOKEN:
        raise ValueError(' BOT TOKEN not set')
    
    if not API_HASH:
        raise ValueError("API_HASH not set")

    if not API_ID:
        raise ValueError("API_ID not set")
