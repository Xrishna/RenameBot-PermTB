import math
import time


async def progress_for_upload(
    current,
    total,
    ud_type,
    message,
    start,
    filename=""
):

    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        # if round(current / total * 100, 0) % 5 == 0:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion

        elapsed_time = TimeFormatter(milliseconds=elapsed_time)
        estimated_total_time = TimeFormatter(milliseconds=estimated_total_time)

        progress = "    ╭───────────────╮\n    │  📊  Progress Bar  📊/n    ╰───────────────╯\n\n   » 📁 File Name : {0} \n╭───────────────────────╮\n│ » 📊 **Status :** Downloding😴.....\n│\n│ » [{1}{2}]\n│\n│ » 📥 **Uploaded :** {3}%".format(
            filename,
            ''.join(["■" for i in range(math.floor(percentage / 5))]),
            ''.join(["▢" for i in range(20 - math.floor(percentage / 5))]),
            round(percentage, 2))

        tmp = progress + "\n│\n│ » ✅**Done :** {0} Of {1}\n│\n️│ » 🚀 Speed : {2}/s\n│\n│ » 🗄 Size : {1}\n│\n│ » ⏱ ETA :  {3}\n╰───────────────────────╯\n\n╭───────────╮\n│🌟Powered By 🌟\n│ » @TeamHP\n│ » @Itsxrishna\n╰───────────╯".format(
            humanbytes(current),
            humanbytes(total),
            humanbytes(speed),
            # elapsed_time if elapsed_time != '' else "0 s",
            estimated_total_time if estimated_total_time != '' else "0 s"
        )
        try:
            await message.edit(
                text="{}\n {}".format(
                    ud_type,
                    tmp
                )
            )
        except:
            pass


def humanbytes(size):
    # https://stackoverflow.com/a/49361727/4723940
    # 2**10 = 1024
    if not size:
        return ""
    power = 2**10
    n = 0
    Dic_powerN = {0: ' ', 1: 'K', 2: 'M', 3: 'G', 4: 'T'}
    while size > power:
        size /= power
        n += 1
    return str(round(size, 2)) + " " + Dic_powerN[n] + 'B'


def TimeFormatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = ((str(days) + "d, ") if days else "") + \
        ((str(hours) + "h, ") if hours else "") + \
        ((str(minutes) + "m, ") if minutes else "") + \
        ((str(seconds) + "s, ") if seconds else "") + \
        ((str(milliseconds) + "ms, ") if milliseconds else "")
    return tmp[:-2]
