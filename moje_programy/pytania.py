import pprint
with open("pytania.csv") as f:
    # reader = f.read()
    l = []
    for r in f.readlines():
        l.append(r.strip().split("/"))

print(l)
d = {k: v for k, v in l}
pprint.pprint(d)
# print(reader.splitlines())

# for line in reader:
#     print(line)
