# TODO


def convert_grade(si):
    s = {}

    for key in si:
        score = si[key]
        if si[key] >= 85:
            s = si
            s[key] = "Outstanding"
        elif si[key] >= 65:
            s = si
            s[key] = "Good"
        elif si[key] >= 50:
            s = si
            s[key] = "Acceptable"
        else:
            s = si
            s[key] = "Fail"

    return s


student_scores = {
    "John": 90,
    "Edy": 68,
    "Marry": 88,
    "Ewan": 79,
    "Park": 62,
}
result = student_scores.pop('John')
print(student_scores)