
# ***************************************** Group 2 ****************************************************

# -------------------------01. The Isle of Man TT Race (Regex/ Text Processing)-------------------------
# -------------------------100 points ------------------------------------------
import re

while True:
    info = input()
    coordinates_found = False

    racer_pattern = r"^[#$%*&][a-zA-Z]+[#$%*&]{1}"  # racer
    racer = re.findall(racer_pattern, info)
    if len(racer) > 0:
        r = racer[0]
        if r[0] == r[-1]:
            racer_name = r.replace('#', '').replace('$', '').replace('%', '').replace('*', '').replace('&', '').replace('=', '')
        else:
            racer_name = ''
    else:
        racer_name = ''

    geohashlength_pattern = r"[=]+[0-9]+"   # geohashcode length
    geohashl = re.findall(geohashlength_pattern, info)
    if len(geohashl) > 0:
        gl = int(geohashl[0].replace('=', ''))
    else:
        gl = 0

    geohashcode_start = info.find('!!')
    geohashcode = info[geohashcode_start+2:]
    decrypted = ''
    for g in geohashcode:
        decrypted += chr(ord(g)+gl)

    if racer_name != '':
        if gl > 0:
            if gl == len(geohashcode):
                coordinates_found = True
                print(f'Coordinates found! {racer_name} -> {decrypted}')
                break
            else:
                print('Nothing found!')
        else:
            print('Nothing found!')
    else:
        print('Nothing found!')
