def stupid_counter(x=[]):
    x.append(0)
    return len(x)


def less_stupid_counter(x=[0]):
    x[0] += 1
    return x[0]

print stupid_counter()
print stupid_counter()
print stupid_counter()
print stupid_counter()
print stupid_counter()
print stupid_counter()
print stupid_counter()
print

print less_stupid_counter()
print less_stupid_counter()
print less_stupid_counter()
print less_stupid_counter()
print less_stupid_counter()
print less_stupid_counter()
print less_stupid_counter()
print

print "Color me surprised"
