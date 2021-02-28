#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

ENTRY = "Bravo6"
CHANNEL = "GPS"

pnconfig = PNConfiguration()
pnconfig.publish_key = "pub-c-71a0a858-0dc8-48ef-a726-8434d244bf56"
pnconfig.subscribe_key = "sub-c-6946f07c-6812-11e9-bedf-bef46dd4efdc"
pnconfig.uuid = "serverUUID-SUB"

pubnub = PubNub(pnconfig)


class MySubscribeCallback(SubscribeCallback):
  def presence(self, pubnub, event):
    print("[PRESENCE: {}]".format(event.event))
    print("uuid: {}, channel: {}".format(event.uuid, event.channel))

  def status(self, pubnub, event):
    if event.category == PNStatusCategory.PNConnectedCategory:
      print("[STATUS: PNConnectedCategory]")
      print("connected to channels: {}".format(event.affected_channels))

  def message(self, pubnub, event):
    print("[MESSAGE received]")

    if event.message["update"] == "42":
      print("The publisher has ended the session.")
      os._exit(0)
    else:
      #print("{}: {}".format(event.message["entry"], event.message["update"]))
      temp=event.message["update"].split()
      print("Latitude: ",temp[1])
      print("Longitude: ",temp[2])
      print("Truck Id: ",temp[0])
      print("Time: ",temp[3],temp[4])
	

pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels(CHANNEL).with_presence().execute()

print("***************************************************")
print("* Waiting for updates to The Guide about {}... *".format(ENTRY))
print("***************************************************")

