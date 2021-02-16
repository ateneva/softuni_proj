
# ********** 02.skeleton (conditional statements) ******************************

control_minutes = int(input())
control_seconds = int(input())
length = float(input())
seconds = int(input())

total_control_seconds = control_minutes * 60 + control_seconds
reduced_timing = (length / 120) * 2.5
marin = (length / 100 ) * seconds - reduced_timing

if marin <= total_control_seconds:
    print(f"Marin Bangiev won an Olympic quota!" )
    print(f"His time is {marin:.3f}.")
else:
    print(f"No, Marin failed! He was {abs(marin - total_control_seconds):.3f} second slower.")
