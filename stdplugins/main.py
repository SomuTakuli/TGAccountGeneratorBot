﻿from telethon import events, Button
from uniborg.util import admin_cmd
import time


channel_id = -1001481026778
msg_id = 211
sticker_delete = False
footer = "\n\n**__➖🔰@PandaZnetwork🔰➖__**"
img = {-1001481026778 : "https://i.imgur.com/fQi4wJe.jpg", -1001481899343 : "https://i.imgur.com/DRUnSIc.jpg", -1001122798596 : "https://i.imgur.com/mGgAIbl.jpg", -1001251394025 : "https://i.imgur.com/NG6M6Eh.jpg", -1001351480003 : "https://i.imgur.com/rhXRIKw.jpg", -1001313593468 : "https://i.imgur.com/tL2awKR.jpg"}
name = {-1001481026778 : "Express VPN", -1001481899343 : "Windscribe", -1001122798596 : "IP Vanish", -1001251394025 : "Hulu", -1001351480003 : "DisneyPlus",  -1001313593468: "Nord VPN"}
paused = False

multiChannelId = {-1001177011841 : "Antivirus"}
multiName = {"Antivirus" : ["mc", "avast", "bd"]}
multiImg = {"mc" : "https://i.imgur.com/UnUErxw.jpg", "avast" : "https://i.imgur.com/fQi4wJe.jpg", "bd" : "https://i.imgur.com/DRUnSIc.jpg"}
multiFullName: {"mc" : "McAfee", "avast": "Avast", "bd": "Bit Defender"}


@borg.on(events.NewMessage)
async def my_event_handler(event):                     
    global channel_id, msg_id, sticker_delete, footer, img, paused, name, multiChannelId, multiName, multiImg, multiFullName
    if channel_id is not None and msg_id is not None and event.chat_id in img.keys():
        if event.text == "/stop":
            paused = True
            await event.edit("Bot Stopped.")
            time.sleep(3)
            await event.delete()
            return
        if event.text == "/start":
            paused = False
            await event.edit("Bot Started.")
            time.sleep(3)
            await event.delete()
            return
        if paused:
            return
        if event.sticker:
            if sticker_delete:
                await event.delete()
        elif event.gif or event.poll or event.media:
            return
        else:
            # try:
            if True:
                if event.chat_id in img.keys():
                    if event.chat_id in name.keys() and ("http://" in event.text.lower() or "https://" in event.text.lower()):
                        msg = f'''**__🔰{name[event.chat_id]}[Valid Hits]🔰

🌀 All accounts are working and fresh. We will never give Not working Accounts

✅ If these accounts have guard then sorry we can't help. 
==========================
⭕️ Link to Accounts :
🔥 {event.text}
==========================
❌ Don't change the password else account will stop soon
➖➖➖➖➖➖➖➖➖➖➖➖
ENJOY ❤️👍

➖🔰@PandaZnetwork🔰➖__**'''
                    else:
                        msg = f"**__🔰{name[event.chat_id]}🔰__**\n\n" + event.text + footer
                    image = img[event.chat_id]
                elif event.chat_id in multiChannelId.keys():
                    print("a")
                    for name in multiName[multiChannelId[event.chat_id]]:
                        print("b", name)
                        if name in event.text:
                            image = multiImg[name]
                            if "|" in event.text:
                                msg = f'''**__🔰{multiFullName[name]}🔰

🌀 All accounts are working and fresh. We will never give Not working Accounts

✅ If these accounts have guard then sorry we can't help. 

🔺 How to Open Links
    Link:- https://youtu.be/XkMSDlGEKqQ
==========================
⭕️ Link to Accounts :
🔥 {event.text[event.text.index("|") + 1 :].strip()}
==========================
❌ Don't change the password else account will stop soon
➖➖➖➖➖➖➖➖➖➖➖➖
ENJOY ❤️👍

➖🔰@PandaZnetwork🔰➖__**'''
                            else:
                                msg = f"**__🔰{multiFullName[name]}🔰__**\n\n" + event.text + footer
                            break
                    else:
                        return
                await event.client.send_message(
                    event.chat_id,
                    msg,
                    file = image,
                    link_preview = False
                )
                await event.delete()
            # except Exception as e:
            #     print(e)
            await borg.forward_messages(event.chat_id, msg_id, channel_id)


