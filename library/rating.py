from library.console import *

class Rating:
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
        
    def skiesEmoji(skies: str):
        """To handle emojis for weather, "Partly Cloudy" would return a specific emoji."""
        if (skies == "Clear"): return "🌈"
        if (skies == "Sunny"): return "☀️"   
        if (skies == "Cloudy"): return "☁️" 
        if (skies == "Rain"): return "💦" 
        if (skies == "Light Rain"): return "💧"   
        if (skies == "Mostly Sunny"): return "🌤️"
        if (skies == "Partly Sunny"): return "⛅"
        if (skies == "Partly Cloudy"): return "🌤️"
        if (skies == "Mostly Cloudy"): return "🌥️"
        if (skies == "Light Rain and Snow"): return "🌨️"
        else: return ""
    
    def precipEmoji(precip: float):
        """To handle precipitation percentage values."""
        if (precip == None): return ""
        if (precip >= 80):
            return "⛈️"
        elif (precip <= 79 and precip >= 50):
            return "🌧️"
        elif (precip <= 49 and precip >= 30):
            return "☔"
        elif (precip <= 29 and precip >= 5):
            return "💧"
        else: 
            return ""        
    
    def checkNum(num: float):
        if (num == None): return 0
        else: return num