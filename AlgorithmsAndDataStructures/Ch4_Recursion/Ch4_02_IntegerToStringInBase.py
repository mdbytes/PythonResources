
def integerToStringInBase(n: int, base: int) -> str:
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return integerToStringInBase(n//base,base) + convertString[n%base]


print(integerToStringInBase(9,10))
print(integerToStringInBase(1,2))
print(integerToStringInBase(255,2))
print(integerToStringInBase(128,2))
print(integerToStringInBase(15000,16))