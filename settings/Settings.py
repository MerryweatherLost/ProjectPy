import random 

# ADMINISTRATION

class Admin:
    """Administration Settings"""
    clearlimit = 20
    """Limit to clear messages."""

class General:
    """List of General Settings."""
    # Console
    def quote():
        quotelist = [
            'Put work into everything that you do.',
            'We created this message just for you.',
            'America grew up listening to us. It still does.',
        ]
        quote = random.choice(quotelist)
        return quote
