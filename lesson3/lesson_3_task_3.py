from address import Address
from mailing import Mailing

to_address = Address("454045", "Челябинск", "Маслобазовая", "7", "8")
from_address = Address("644082", "Омск", "Южная", "60", "5")

mailing = Mailing(to_address, from_address, 800, "TREK880054545")

print(mailing)
