from time import strftime
from typing import Any, Iterable, List, Type

LOG_PATH = "./common.log"
TIME_FMT = "%Y/%m/%d %H:%M:%S"


def log(message: str, message_type: str):
    line = "[{}] {}: {}\n".format(strftime(TIME_FMT), message_type, message)
    output = open(LOG_PATH, "a")
    output.write(line)
    output.close()
