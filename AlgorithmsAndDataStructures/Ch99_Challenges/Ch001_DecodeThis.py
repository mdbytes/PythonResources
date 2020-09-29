"""
Hint:  k -> m, o ->q, e -g

"""

aString = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr\n amknsrcpq ypc dmp. bmgle gr gl zw fylb gq\n glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.\n sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw\n ml rfc spj."

print(aString)

alphaBet = "abcdefghijklmnopqrstuvwxyz"

decode_key = "yzabcdefghijklmnopqrstuvwx"

decoded_string = ""

for char in aString:
    if char.isalpha():
        decoded_string += alphaBet[decode_key.index(char)]
    else:
        decoded_string += char

print(decoded_string)



