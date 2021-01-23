
# ***************************************** Group 1 ****************************************************

# -------------------------01. Arriving in Katmandu (Regex/ Text Processing)---------------------------
# --------------------40 points -------------------------------
import re
info = input()

while info != 'Last note':
    coordinates_found = False

    # peak name
    peak_pattern = r"\w[!@#$?a-zA-Z0-9]+[=]"
    peak = re.findall(peak_pattern, info)
    if len(peak) > 0:
        peak_name = peak[0].replace('!', '').replace('@', '').replace('#', '').replace('$', '').replace('?','').replace('=', '')
    else:
        peak_name = ''

    # geohashcode length
    geohashlength_pattern = r"[=]+[0-9]+"
    geohashl = re.findall(geohashlength_pattern, info)
    if len(geohashl) > 0:
        gl = int(geohashl[0].replace('=', ''))
    else:
        gl = 0

    # geohashcode
    geohashcode_pattern = r"[<<]+[a-z[0-9]+"
    geohashcode = re.findall(geohashcode_pattern, info)[0].replace('<<', '')

    if peak_name != '':
        if gl > 0:
            if gl == len(geohashcode):
                coordinates_found = True

    if coordinates_found:
        print(f'Coordinates found! {peak_name} -> {geohashcode}')
    else:
        print('Nothing found!')

    info = input()
