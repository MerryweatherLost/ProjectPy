from datetime import datetime
import random

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

    def timeFormatUniversial():
        """
        Sets the time format, UTC.

        Variables
        -----------
        formTime:
            variable from date_object.strftime("%H:%M:%S - %b %d %Y") to cut down drastically on size. 
            It will be used in console logging. 
        """
        date_object = datetime.utcnow()
        formTime = date_object.strftime("%H:%M UTC - %b %d, %Y")

        return formTime

class Essentials:
    def response8ball():
        """
        Responses handler for a randomized 8ball.

        Variables
        ---------
        responses: `str`, `list`,

        List of literal strings to pull from later on.

        response8ball: `var`,

        Picks one literal string from a `random.choice` function.
        """
        responses = [
            # POSITIVES
            'It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes.',
            'Outlook good.', 'Signs point to yes.', 'That is correct.',
            'Indeed.', 'Affirmative.',
            # NEUTRALS
            'Reply hazy, try again.',
            'Ask again later.','Can not predict now.', 
            'I can not find a result for that, try again.','Try again.',
            # NEGATIVES
            "Don't count on it.", 'My reply is no.', 'My sources say no.', 
            'Obviously not.', 'Negative.','Absolutely false.','Decidedly not.',
            'No.', 'That is incorrect.'
        ]
        response8ball = random.choice(responses)

        return response8ball

    def ballImage():

        ballImage = 'https://cdn.discordapp.com/attachments/576096750331494420/896414018133196800/8b.png'
        
        return ballImage

    def CoinToss():
        """
        Responses handler for a randomized coinflip.

        Variables
        ---------
        responses: `str`, `list`,

        List of literal strings to pull from later on.

        coinflip: `var`,

        Picks one literal string from a `random.choice` function.
        """
        responses = [ 'Heads.','Tails.' ]
        
        coinflip = random.choice(responses)
        
        return coinflip