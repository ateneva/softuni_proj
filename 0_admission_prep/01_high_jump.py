
# *********** 06.high jump (nested loop) ***************************************
target = int(input())
first_target = target - 30
jumps = 0
fail = 0

while first_target <= target:
    for attempt in range(1, 4):
        next_jump = int(input())
        jumps += 1

        if next_jump > first_target:
            first_target += 5
            fail = 0
            break
        else:
            fail += 1

    if fail == 3:
        print(f"Tihomir failed at {next_jump}cm after {jumps} jumps.")
        break

else:
    print(f"Tihomir succeeded, he jumped over {target}cm after {jumps} jumps.")
