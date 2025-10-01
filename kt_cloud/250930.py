import csv

# csv 파일 호출하기
def to_csv(_list):
    file = open('data_1.csv', 'w', encoding='utf-8', newline='')
    for row in _list:
        write_row = ''
        for element in row:
            write_row += f"{element},"
        file.write(write_row+'\n')
    file.close()

#to_csv(['1', '2', '3', '4'])
to_csv([['1', '2'], ['3', '4']])

# 한 열에 csv 입력
def to_csv(_list):
    file = open('data_2.csv', 'w', encoding='utf-8', newline='')
    csvfile = csv.writer(file)
    for row in _list:
        csvfile.writerow(row)

to_csv([['1', '2'], ['3', '4']])
