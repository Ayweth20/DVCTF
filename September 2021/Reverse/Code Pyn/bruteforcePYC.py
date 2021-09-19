import marshal, dis

f = open('pyn.pyc', 'rb')
f.seek(16)
co = marshal.load(f)
print(dis.dis(co))
