# import message_activity
# from message_activity import *
# from message_activity import show_messages, send_messages
# import message_activity as ma
from message_activity import show_messages as show
from message_activity import send_messages as send

print("--------------Exercise 8-9------------------")
recentTexts = ['need anything from the grocery store?', 'yep, eggs are already on my list', 'is that all?', 'ok, probably home by 7','can you feed the cat?']

show(recentTexts)

print("--------------Exercise 8-10------------------")
sent_messages = []

send(recentTexts,sent_messages)
print(recentTexts)
print(sent_messages)

print("--------------Exercise 8-11------------------")
sent_messages = []
recentTexts = ['need anything from the grocery store?', 'yep, eggs are already on my list', 'is that all?', 'ok, probably home by 7','can you feed the cat?']

send(recentTexts[:])
print(recentTexts)
print(sent_messages)