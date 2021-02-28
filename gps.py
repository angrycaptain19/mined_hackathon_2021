
import sys
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
import time
import random
from datetime import datetime

ENTRY = "Bravo6"
CHANNEL = "GPS"
the_update = None
n=sys.argv[1]
pnconfig = PNConfiguration()
pnconfig.publish_key = "pub-c-71a0a858-0dc8-48ef-a726-8434d244bf56"
pnconfig.subscribe_key = "sub-c-6946f07c-6812-11e9-bedf-bef46dd4efdc"
pnconfig.uuid = "serverUUID-PUB"

pubnub = PubNub(pnconfig)

print("*****************************************")
print("* Submit updates *")
print("*     Enter 42 to exit this process     *")
print("*****************************************")

while the_update != "42":
    
    the_update = n+" "+ str(random.randrange(68,97))+" "+ str(random.randrange(8,37))+ " "+datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    the_message = {"entry": ENTRY, "update": the_update}
    envelope = pubnub.publish().channel(CHANNEL).message(the_message).sync()
    print(n)
    if envelope.status.is_error():
        print("[PUBLISH: fail]")
        print("error: %s" % status.error)
    else:
        print("[PUBLISH: sent]")
        print("timetoken: %s" % envelope.result.timetoken)
    time.sleep(1)

