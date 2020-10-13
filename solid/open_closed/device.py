from abc import ABC, abstractmethod


class Device(ABC):
    @abstractmethod
    def turnOn(self):
        pass

    @abstractmethod
    def turnOff(self):
        pass


class TV(Device):
    def turnOn(self):
        self.switch_to_fav_channel()
        print('Turned Tv On')

    def turnOff(self):
        print('Turned Tv off')

    def switch_to_fav_channel(self):
        print('Switched to favorite channel')

    def turn_on_tv_recording(self):
        print('Turned on tv recording')

    def __str__(self):
        return "Television"


class Projector(Device):
    def turnOn(self):
        self.pull_down_projector_screen()
        print('Turned Projector On')

    def turnOff(self):
        self.pull_up_projector_screen()
        print('Turned Projector off')

    def pull_up_projector_screen(self):
        print('Pulled up screen')

    def pull_down_projector_screen(self):
        print('Pulled down screen')

    def __str__(self):
        return "Projector"


class SurroundSoundSystem(Device):
    def turnOn(self):
        self.increase_volume()
        print('Turned Surround sound On')

    def turnOff(self):
        self.decrease_volume()
        print('Turned Surround sound off')

    def increase_volume(self):
        print('Increased volume')

    def decrease_volume(self):
        print('Decreased volume')

    def __str__(self):
        return "Surround Sound System"