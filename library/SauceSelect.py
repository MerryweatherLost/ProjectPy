from pysaucenao import *
from library.ConsoleSelect import *

class SauceSelect:
    def similarEmoji(sim: float):
        """To handle simple emojis based on probability count. `float`."""
        if (sim > 90):
            return "<a:cleo:902025889179631637>"
        elif (sim <= 89 and sim >= 70):
            return "<a:checkmark:903852585360949289>"
        elif (sim <= 69 and sim >= 40):
            return "🤔"
        else:
            return "⛔"
    
            
