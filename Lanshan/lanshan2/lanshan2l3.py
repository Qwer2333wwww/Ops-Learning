def judge(score):
    if score >100 or score <0:
        return "Invalid score"
    elif score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

raw_input = input("Enter your score: ")
score = int(raw_input)
print(judge(score))