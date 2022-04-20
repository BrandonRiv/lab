class Television:
    '''
    A class representing details for a Television object
    Min and Max channel variables stored - MIN = 0 and MAX = 3
    Min and Max volume variables stored - MIN = 0 and MAX = 2
    '''
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    MIN_VOLUME = 0
    MAX_VOLUME = 2

    def __init__(self) -> None:
        '''
        Constructor to create initial state of a Television object.
        :var1 self.__channel: Set default channel to MIN_CHANNEL
        :var2 self.__volume: Set default volume to MIN_VOLUME
        :var3 self.__status: Set default to False
        '''
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__status = False


    def power(self) -> None:
        '''
        Method to power on/off the television
        '''
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False


    def channel_up(self) -> None:
        '''
        Method to move the channel up by 1
        '''
        if self.__status and self.__channel < Television.MAX_CHANNEL:
            self.__channel += 1
        elif self.__status and self.__channel == Television.MAX_CHANNEL:
            self.__channel = 0


    def channel_down(self) -> None:
        '''
        Method to move the channel down by 1
        '''
        if self.__status and self.__channel > Television.MAX_CHANNEL:
            self.__channel -= 1
        elif self.__status and self.__channel == Television.MIN_CHANNEL:
            self.__channel = 3


    def volume_up(self) -> None:
        '''
        Method to move the volume up by 1
        '''
        if self.__status and self.__volume < Television.MAX_VOLUME:
            self.__volume += 1
        elif self.__status and self.__volume == Television.MAX_VOLUME:
            self.__volume = 2



    def volume_down(self) -> None:
        '''
        Method to move the volume down by 1
        '''
        if self.__status and self.__volume > Television.MIN_VOLUME:
            self.__volume -= 1
        elif self.__status and self.__volume == Television.MIN_VOLUME:
            self.__volume = 0



    def __str__(self) -> str:
        '''
        Method to return and print the TV status, current channel, and current volume
        '''
        return f'TV Status : Is on = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'