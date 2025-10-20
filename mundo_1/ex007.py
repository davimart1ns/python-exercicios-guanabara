d = float(input('Uma distância em metros: '))
km = d / 1000
hm = d / 100
dam = d / 10
dm = d * 10
cm = d * 100
mm = d * 1000
print('A medida de {}m corresponde a {}km, {}hm, {}dam, {:.0f}dm, {:.0f}cm e {:.0f}mm'.format(d, km, hm, dam, dm, cm, mm))