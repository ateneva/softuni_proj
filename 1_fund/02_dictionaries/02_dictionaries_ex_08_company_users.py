
# -----------------------------08. Company Users -------------------------------

'''
Write a program that keeps information about companies and their employees.
Until you receive the "End" command, you will be receiving input
    in the format: "{companyName} -> {employeeId}".

Add each employee to the given company.
Keep in mind that a company cannot have two employees with the same id.

When you finish reading the data, order the companies by the name in ascending order.
Print the company name and each employee's id in the following format:
    {companyName}
    -- {id1}
    -- {id2}
    -- {idN}
'''

# --------------100 points --------------------
comp_users = input()
companies = {}

while comp_users != 'End':
    comp_users = comp_users.split(' -> ')
    company = comp_users[0]
    user = comp_users[1]

    if company not in companies:
        companies[company] = [user]     # create dictioanry key if it does not exist
    else:
        for k, u in companies.items():
            if k == company and user not in u:
                companies[company].append(user)

    comp_users = input()

#print(companies)
companies = dict(sorted(companies.items(), key=lambda s: s[0]))

#print(companies)

for k, v in companies.items():
    print(k)
    for c in v:
        print(f'-- {c}')
