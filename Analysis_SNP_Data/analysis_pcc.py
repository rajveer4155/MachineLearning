# Instructions to run the code: #
# python proj.py [traindata] [trueclass] [testdata]

import sys
import math


def pcc(x, y):
    col_correlation = []
    rows = len(x)
    cols = len(x[0])
    mean_y = 0
    sd_y = 0
    for j in range(rows):
        mean_y += y[j]
    mean_y /= rows
    for j in range(rows):
        sd_y += (mean_y - y[j]) * (mean_y - y[j])
    sd_y = math.sqrt(sd_y)
    for j in range(cols):
        num = 0
        mean_x = 0
        sd_x = 0
        for i in range(rows):
            mean_x += x[i][j]
        mean_x /= rows
        for i in range(rows):
            sd_x += (mean_x - x[i][j]) * (mean_x - x[i][j])
        sd_x = math.sqrt(sd_x)
        for i in range(rows):
            num += (mean_x - x[i][j]) * (mean_y - y[i])
        den = sd_y * sd_x
        if den == 0:
            r = 0
        else:
            r = num / den
        if r < 0:
            r *= -1
        col_correlation.append(r)
    return col_correlation

print('Expected finish time: 5 mins...')
datafile = sys.argv[1]
f = open(datafile)
data = []

l = f.readline()
while l != '':
    a = l.split()
    l2 = []
    for j in range(0, len(a), 1):
        l2.append(int(a[j]))
    data.append(l2)
    l = f.readline()

rows = len(data)
cols = len(data[0])

f.close()

label_file = sys.argv[2]
f = open(label_file)
y = []
n = [0, 0]

l = f.readline()
while l != '':
    a = l.split()
    y.append(int(a[0]))
    n[int(a[0])] += 1
    l = f.readline()
f.close()

col_correlation = pcc(data, y)

corr_len = len(col_correlation)

selected = []

for i in range(0, corr_len, 1):
    if col_correlation[i] > 0.095:
        selected.append(i)

print('\n No. of features:\t ', len(selected))
#print('\n Selected features:\n', selected)

new_data = []

for i in range(0, len(data), 1):
    temp = []
    for j in range(0, len(selected), 1):
        k = selected[j]
        temp.append(int(data[i][k]))
    new_data.append(temp)

rows = len(new_data)
cols = len(new_data[0])

testfile = sys.argv[3]
f = open(testfile)
test_data = []

l = f.readline()
while l != '':
    a = l.split()
    l2 = []
    for j in range(0, len(selected), 1):
        k = selected[j]
        l2.append(int(a[k]))
    test_data.append(l2)
    l = f.readline()

m0 = []
m1 = []

for i in range(0, cols, 1):
    m0.append(0)
    m1.append(0)

for i in range(0, rows, 1):
    if y[i] == 0:
        for j in range(0, cols, 1):
            m0[j] += new_data[i][j]
    elif y[i] == 1:
        for j in range(0, cols, 1):
            m1[j] += new_data[i][j]

for j in range(0, cols, 1):
    m0[j] /= n[0]
    m1[j] /= n[1]

file = open('prediction', 'w')

for i in range(0, len(test_data), 1):
    d0 = 0
    for j in range(0, cols, 1):
        d0 += (m0[j] - test_data[i][j]) ** 2

    d1 = 0
    for j in range(0, cols, 1):
        d1 += (m1[j] - test_data[i][j]) ** 2

    if d0 < d1:
        #print('0', i)
        file.write('0' + ' ' + str(i) + '\n')
    else:
        #print('1', i)
        file.write('1' + ' ' + str(i) + '\n')
file.close()
