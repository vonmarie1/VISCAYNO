rat = (1924, 1936, 1948, 1960, 1972, 1984, 1996, 2008, 2020)
ox = (1925, 1937, 1949, 1961, 1973, 1985, 1997, 2009, 2021)
tiger = (1926, 1938, 1950, 1962, 1974, 1986, 1998, 2010, 2022)
rabbit = (1927, 1939, 1951, 1963, 1975, 1987, 1999, 2011, 2023)
dragon = (1928, 1940, 1952, 1964, 1976, 1988, 2000, 2012, 2024)
snake = (1929, 1941, 1953, 1965, 1977, 1989, 2001, 2013, 2025)
horse = (1930, 1942, 1954, 1966, 1978, 1990, 2002, 2014, 2026)
goat = (1931, 1943, 1955, 1967, 1979, 1991, 2003, 2015, 2027)
monkey = (1932, 1944, 1956, 1968, 1980, 1992, 2004, 2016, 2028)
rooster = (1933, 1945, 1957, 1969, 1981, 1993, 2005, 2017, 2029)
dog = (1934, 1946, 1958, 1970, 1982, 1994, 2006, 2018, 2030)
pig = (1935, 1947, 1959, 1971, 1983, 1995, 2007, 2019, 2031)

zodiac = eval(input("What is your birth year?"))

if zodiac in rat:
    print("Your Chinese Zodiac sign is Rat.")
elif zodiac in ox:
    print("Your Chinese Zodiac sign is Ox.")
elif zodiac in tiger:
    print("Your Chinese Zodiac sign is Tiger.")
elif zodiac in rabbit:
    print("Your Chinese Zodiac sign is Rabbit.")
elif zodiac in dragon:
    print("Your Chinese Zodiac sign is Dragon.")
elif zodiac in snake:
    print("Your Chinese Zodiac sign is Snake.")
elif zodiac in horse:
    print("Your Chinese Zodiac sign is Horse.")
elif zodiac in goat:
    print("Your Chinese Zodiac sign is Goat.")
elif zodiac in monkey:
    print("Your Chinese Zodiac sign is Monkey.")
elif zodiac in rooster:
    print("Your Chinese Zodiac sign is Rooster.")
elif zodiac in dog:
    print("Your Chinese Zodiac sign is Dog.")
elif zodiac in pig:
    print("Your Chinese Zodiac sign is Pig.")
else:
    print("Invalid Zodiac Year \nThe year you suggested does not exist in the Chinese Calendar.")