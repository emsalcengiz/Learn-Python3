from device import TV, Projector, SurroundSoundSystem
from remotecontrol import RemoteControl


def main():
    tv = TV()
    projector = Projector()
    sound_system = SurroundSoundSystem()
    remote = RemoteControl()
    remote.connect_to_device(tv)
    remote.clickOnButton()
    remote.clickOffButton()
    remote.connect_to_device(projector)
    remote.clickOnButton()
    remote.clickOffButton()
    remote.connect_to_device(sound_system)
    remote.clickOnButton()
    remote.clickOffButton()


main()