metros = float(input('Digite a distancia em metros: '))
dm = metros * 10
cm = metros * 100
mm = metros * 1000
km = metros / 1000
hm = metros / 100
dam = metros / 10
print(f'O valor de {metros:.0f}m eh {km}km, {hm}hm, {dam}dam, {dm:.0f}dm, {cm:.0f}cm e {mm:.0f}mm')