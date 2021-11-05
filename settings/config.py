import random 

# ADMINISTRATION

version = '1.3.0'

class Admin:
    """Administration Settings"""
    clearlimit = 20
    """Limit to clear messages."""

class General:
    """List of General Settings."""
    # Console
    def quote():
        quotelist = [
            u'\u001b[34;1mHey, who turned the lights off?\u001b[0m',
            u'\u001b[34;1mAmerica grew up listening to us. It still does.\u001b[0m',
        ]
        quote = random.choice(quotelist)
        return quote
