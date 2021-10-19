import random 

# ADMINISTRATION

version = '1.1.0'

class Admin:
    """Administration Settings"""
    clearlimit = 20
    """Limit to clear messages."""

class General:
    """List of General Settings."""
    # Console
    def quote():
        quotelist = [
            u'\u001b[33;1mPut work into everything that you do.\u001b[0m',
            u'\u001b[33;1mWe created this message just for you.\u001b[0m',
            u'\u001b[33;1mAmerica grew up listening to us. It still does.\u001b[0m',
        ]
        quote = random.choice(quotelist)
        return quote
