
# -------------------------04. capitals ---------------------------------------

'''
write a program that receives countries on the first line separated by comma
and space ", " and their corresponding capital cities on the second line
(again separated by comma and space ", ")

Print each country with their capital on a separate line in the format:
    "{country} -> {capital}"

'''

# approach 1: use two dictionaries
def get_capitals(country_seq, captial_seq):
    countries = country_seq.split(", ")
    capitals = captial_seq.split(", ")

    final_dict ={}
    for country in countries:
        for capital in capitals:
            if capitals.index(capital) == 0:
                country_dict = {
                    country: capital
                }

                final_dict.update(country_dict)
                del capitals[0]

    return final_dict

capital_reference = get_capitals(input(), input())
for ctry, capl in capital_reference.items():
    print(f'{ctry} -> {capl}')

# approach 2: use dictionary comprehension
def get_capital_reference(country_seq, captial_seq):
    countries = country_seq.split(", ")
    capitals = captial_seq.split(", ")
    reference ={country: capital
                for (country, capital) in zip(countries,capitals)
    }

    return reference

capital_reference = get_capital_reference(input(), input())
for ctry, capl in capital_reference.items():
    print(f'{ctry} -> {capl}')
