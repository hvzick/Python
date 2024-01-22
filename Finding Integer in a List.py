# custom_list = [11, 30.1, 90.2, 30, 45.1, 54, '54']
#
# for inte in custom_list:
#     if type(inte) is int:
#         print(inte)
#

student_scores = [80, 60, 50, 65, 75, 55]

def sum(student_scores):
    ss =0
    ns = 0
    for score in student_scores:
        ss += score
        ns += 1
    avgs = ss/ ns
    sav = 0
    for score in student_scores:
        if score > avgs:
            sav += score
    return sav
print(sum(student_scores))
