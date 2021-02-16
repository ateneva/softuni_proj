
# train the trainers -----------------------------------------------------------

jury = int(input())
presentation = input()
total_score = 0
total_avg_score = 0
presentation_count = 0

while not presentation == 'Finish':
    avg_score = 0  # nullify avg_score fpr every presentation
    total_score = 0

    for i in range(1, jury + 1):
        score = float(input())
        total_score += score
        total_avg_score += score
        presentation_count += 1

    avg_score = total_score / jury
    print(f'{presentation} - {avg_score:.2f}.')

    presentation = input()

else:
    total_avg_score /= presentation_count
    print(f"Student's final assessment is {total_avg_score:.2f}.")
