import time
import math
import os
from Easy_F import hrb, hrt
from pyrogram.errors import FloodWait

class Timer:
    def __init__(self, time_between=5):
        self.start_time = time.time()
        self.time_between = time_between

    def can_send(self):
        if time.time() > (self.start_time + self.time_between):
            self.start_time = time.time()
            return True
        return False

timer = Timer()

async def progress_bar(current, total, reply, start):
    if timer.can_send():
        now = time.time()
        diff = now - start
        if diff < 1:
            return
        else:
            perc = f"{current * 100 / total:.1f}%"
            elapsed_time = round(diff)
            speed = current / elapsed_time
            sp = str(hrb(speed)) + "ps"
            tot = hrb(total)
            cur = hrb(current)

            remaining_items = total - current
            if speed == 0:
                eta = "Calculating..."
            else:
                eta_seconds = remaining_items / speed
                eta = hrt(eta_seconds)

            bar_length = 20
            progress = current / total
            num_blocks = math.floor(bar_length * progress)

            # Unicode block characters to create the progress bar
            full_block = '█'
            empty_block = '░'
            bar = f"{full_block * num_blocks}{empty_block * (bar_length - num_blocks)}"

            try:
                await reply.edit(f'`╔═ ◣━━━🄿🅁🄰🄳🄷🄰🄽 🄹🄸━━━◢\n'
                                 f'║ {bar} \n'
                                 f'║ 𝙋𝙧𝙤𝙜𝙧𝙚𝙨𝙨 ⏳- {perc} \n'
                                 f'║ 𝙎𝙥𝙚𝙚𝙙 ⚡ - {sp} \n'
                                 f'║ 𝗗𝗼𝗻𝗲 💾- {cur}\n'
                                 f'║ 𝗧𝗼𝘁𝗮𝗹 💿- {tot}\n'   
                                 f'║ 𝙀𝙏𝘼 🕒 - {eta}\n'           
                                 f'╚══◢`')
            except FloodWait as e:
                time.sleep(e.x)

# Usage example:
# Call the progress_bar function with the appropriate arguments:
# current - current progress value
# total - total items to be processed
# reply - a reference to the message object where the progress bar will be displayed
# start - the timestamp when the progress started (time.time() at the beginning)

                                 
