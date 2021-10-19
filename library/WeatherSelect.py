import python_weather

class Weather():
    metric = python_weather.METRIC
    imperial = python_weather.IMPERIAL 

    def standard(standard):
        if (standard != None):
            str.lower(standard)
        else:
            standard = 'imperial'

        if (standard == 'metric'): STN = Weather.metric
        elif (standard == 'imperial'): STN = Weather.imperial
        else: STN = Weather.imperial
        return STN