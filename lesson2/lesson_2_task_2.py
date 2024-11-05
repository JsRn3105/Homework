def is_year_leap(year):
    return year % 4 == 0


year = int(input("Введите год: "))
is_leap = is_year_leap(year)
print(f"Год {year}: {is_leap}")
