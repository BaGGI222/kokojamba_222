class Year:
    def __init__(self, days, season):
        self.__days = days
        self.__season = season
    
    def get_days(self):
        return self.__days 
    def get_season(self):
        return self.__season
    
    def set_days(self, days):
        if days == 365 or days == 366:
            self.__days = days
        else:
            raise Exception('Некорректное значение')

    def set_season(self, season):
        self.__season = season

year = Year(365, 'summer')
year.set_days(300)
print(year.get_days(), year.get_season(), sep = '\n')