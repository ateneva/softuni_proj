
# hospital---------------------------------------------------------------------

period = int(input())
total_treated = 0
total_untreated = 0
treated_patients = 0
untreated_patients = 0
doctors = 7

for day in range(1, period + 1):
    patients = int(input())

    if patients <= doctors:
        treated_patients += patients
    else:
        treated_patients += doctors
        untreated_patients += (patients - doctors)

    if day % 3 == 0 and untreated_patients >= treated_patients:
        doctors += 1
        treated_patients += 1
        untreated_patients -= 1

total_treated += treated_patients
total_untreated += untreated_patients
print(f'Treated patients: {total_treated}.')
print(f'Untreated patients: {untreated_patients}.')
