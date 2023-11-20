cfgGO = open('csgo.cfg').read()
cfg2 = cfgGO.replace('r_cleardecals', '') + '\nbind "MOUSE_X" "yaw"\nbind "MOUSE_Y" "pitch"'
changes = open('changes.txt').read().split('\n')
removes = open('removes.txt').read().split('\n')
speeds = ['sv_noclipspeed', 'sv_specspeed']

if '+jump;-attack;-attack2;-jump' in cfgGO:
    cfg2 += '\nalias "jumpthrow" "+jump;-attack;-attack2;-jump"'
    cfg2 = cfg2.replace('+jump;-attack;-attack2;-jump', 'jumpthrow')

for i in changes:
    cfg2 = cfg2.replace(i.split()[0], i.split()[1])
cfg2Lines = cfg2.split('\n')
cfg2 = ''
for i in cfg2Lines:
    if i and i.split()[0] not in removes:
        if i.split()[0] not in speeds: cfg2 += i + '\n'
        else: cfg2 += i.split()[0] + ' "1200"\n'
open('cs2.cfg', 'w').write(cfg2)