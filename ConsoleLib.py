from datetime import datetime

class Time:
    """

    ConsoleLib.Time
    ~~~~~~~~~~~~~~~~~~~~~
    Time class for the Console Library.

    Created by: Raymond Allison

    """
    
    def timeFormat():
        """
        Sets the time format.

        Variables
        -----------
        formTime:
            variable from date_object.strftime("%H:%M:%S - %b %d %Y") to cut down drastically on size. 
            It will be used in console logging. 
        """
        date_object = datetime.now()
        formTime = date_object.strftime("%H:%M:%S - %b %d %Y")

        return formTime

class Essentials:
    def roundTrip(self):
        roundtrip = round(self.client.latency * 1000) + 'ms.'
        return roundtrip