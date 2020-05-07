statement = "Where now? Who now? When now?"
d = '?'

split_list = [e + d for e in statement.split(d) if e]

print(split_list)

# https://stackoverflow.com/questions/7866128/python-split-without-removing-the-delimiter