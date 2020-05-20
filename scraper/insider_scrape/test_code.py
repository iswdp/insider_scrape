symbols

failed_list

dropped = []

for i in range(len(symbols)-1):
    if symbols[i] in failed_list:
        temp = symbols.pop(i)
        dropped.append(temp)