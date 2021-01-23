
# https://github.com/ateneva/softuni_proj/wiki/fund_20200407_mid_exam_retake

# --------------------------02. Shoot for the Win (Basic Lists)---------------------------
# ----------------- 90 points --------------------------------

targets = list(map(lambda x: int(x), input().split(' ')))
command = input()
shot_targets = []

while command != 'End':
    idx = int(command)  # target to be shot

    if idx < len(targets) and idx not in shot_targets:
        original_target = targets[idx]
        targets[idx] = -1             # shoot a target
        shot_targets.append(idx)

        for t in targets:
            if t != -1:                   # make sure you don't update values of shot targets
                t_idx = targets.index(t)  # remember index to update
                if t > original_target:
                    targets[t_idx] -= original_target
                else:
                    targets[t_idx] += original_target

    command = input()

format_print = ' '.join(list(map(lambda x: str(x), targets)))
print(f"Shot targets: {len(shot_targets)} -> {format_print}")
