
# # https://github.com/ateneva/softuni_proj/wiki/fund_20200705_mid_exam

# --------------------03. Numbers  (Lists Advanced)---------------------------
# ------------------- 100 points --------------------------

elements = list(map(lambda x: int(x),input().split(' ')))
avg_value = sum(elements) / len(elements)

new_sequence = [e for e in elements if e > avg_value]
filtered_list = list(map(lambda x: str(x),sorted(new_sequence, reverse=True)))[:5]

if len(filtered_list) > 0:
    print(' '.join(filtered_list))
else:
    print('No')
