import enum

@enum.unique
class LogLevel(enum.IntEnum):
    ERROR = 1
    DEBUG = 2
    WARNİNG = 3
    # FATAL = enum.auto()
    # INFO = enum.auto()
    # CRITIC = enum.auto()

#  print(len(LogLevel))
for level in LogLevel:
    print("{}->{}".format(level.name, level.value))



def log(level, message):
    print("{}:{}:{}".format(level.name,level.value, message))


log(LogLevel.ERROR, "Bu bir hata mesajıdır..")