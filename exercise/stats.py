import matplotlib.pyplot as plt

try:
    exer = open('StudentExercise.csv')
except:
    print("File cannot be opened. PLease try again.")
    exit()

next(exer)
d = dict()
for line in exer:
    e_data = line.split(',')
    e_hours = e_data[0]
    if e_hours != '':
        hr = float(e_hours)
        d[hr] = d.get(hr,0) + 1


plt.hist(d)

plt.ylabel('Occurences')
plt.title('Hours of Exercise')

plt.show()

def student_count(d):
    num = 0.0
    for val in d:
        num = num + val
    return num

num_students = student_count(d)


def average(d):
    big_num = 0
    for key, val in d.items():
        big_num = (key * val) + big_num
    mean = big_num/num_students
    return mean

#mean needs to get the average of the hours. hours are in dictionary. so.
#  have two numbers going. one is the total number of students, which would
#  be all of the vals added together. the other is the weighted data.
#  which would be key * val for each pair in dict, then divided by the
#  number of students.


def prop_above(d):
    students_abv = 0
    num = 0
    avg_hrs = average(d)
    for key, val in d.items():
        if key > avg_hrs:
            students_abv = val + students_abv
            num += 1
    div = students_abv/num_students
    return div

print("The average number of hours is {:.2f}".format(average(d)))
print("The percentage of students above average is {0:.0%}".format(prop_above(d)))



#apologies in advance for this extremely stupid and convoluted way to
# calculate the median.
#
#nevermind i gave up. it is late and i don't want to miss turning it in.
# I may try working on it again tomorrow and update the github to match.
# I will leave a note along with the obvious edit commit history if I do.

def median(d):
    ls = list(d.keys())
    ls.sort()
    if num_students % 2 == 1:
        mid = (len(ls)/2) - 0.5
        med = ls[mid]
    else:
        mid1 = (len(ls)/2)
        mid2 = mid1-1
        med = (mid1 + mid2)/2
    return med
        
print("The median number of hours is {:.2f}".format(median(d)))

#no dict needed
#.len()
