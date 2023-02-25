# script display value of list of tuples championsLeagueWinners in a table in the console
championsLeagueWinners = [('Inter Milan', 2010, 27),
    ('Fc Barcelona', 2010, 27),
    ('Chelsea', 2011, 32),
    ('Inter Milan', 2012, 45),
    ('Bayern Munchen', 2013, 27),
    ('Real Madrid', 2014, 33),
    ('Fc Barcelona', 2015, 42),
    ('Real Madrid', 2016, 47),
    ('Real Madrid', 2017, 33),
    ('Real Madrid', 2018, 45),
    ('Liverpool', 2019, 34),
    ('Bayern Munchen', 2020, 25)
]

print("{0:16} {1:12} {2:12}".format("Team", "Year Won", "Goals Scored"))
print("-"*46)
for element in championsLeagueWinners:
    print("{0:16} {1:^12} {2:^12}".format(element[0], element[1], element[2]))
