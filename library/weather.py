import python_weather

class Weather():
    metric = python_weather.METRIC
    imperial = python_weather.IMPERIAL 

    def standard(stn):
        """Returns the specific standard baseed on entry."""
        str.lower(stn)
        if stn == 'metric': return python_weather.METRIC
        else: return python_weather.IMPERIAL
        
    def scale_name(stn):
        """Scales the name of the standard."""
        if stn == 'C': return "Celsius"
        if stn == 'F': return "Fahrenheit"