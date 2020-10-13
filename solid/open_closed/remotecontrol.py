class RemoteControl:
    __device = None
    __remote = None

    def __init__(self):
        if not RemoteControl.__remote:
            print(" Constructor called..")
        else:
            print("Instance already exists:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = RemoteControl()
        return cls.__remote

    def connect_to_device(self, device):
        self.__device = device
        print(f"Connected to {device}")

    def clickOnButton(self):
        if self.__device is None:
            raise Exception("No Device connected")
        self.__device.turnOn()

    def clickOffButton(self):
        if self.__device is None:
            raise Exception("No Device connected")
        self.__device.turnOff()


class RemoteControlBad:
    __remote = None

    def __init__(self):
        if not RemoteControl.__remote:
            print(" Constructor called..")
        else:
            print("Instance already exists:", self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = RemoteControl()
        return cls.__remote

    def turn_on_tv(self):
        pass

    def turn_off_tv(self):
        pass

    def turn_on_projector(self):
        pass

    def turn_off_projector(self):
        pass