from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13", "+799999999999"),
    Smartphone("Samsung", "Galaxy s24 Ultra", "+78888888888"),
    Smartphone("Huawei", "P60 Pro", "+77777777777"),
    Smartphone("Xiaomi", "Redmi Note 13 Pro", "+76666666666"),
    Smartphone("Google", "Pixel 9 Pro XL", "+75555555555")
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} "
          f"- {smartphone.phone_number}")
