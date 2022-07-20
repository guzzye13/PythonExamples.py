#dog years converter
#input dog years
#output human years
def dog_year_converter(years):
    years = int(years)
    if years < 0:
        return "Please enter any age over 0."
    return years * 7


age = input("Dog's age: ")
print("Converted to human years:", dog_year_converter(age))
