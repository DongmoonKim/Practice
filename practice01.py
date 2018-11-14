import csv
import datetime

now = datetime.datetime.now()
dateTime1 = now.strftime('%m/%d/%Y')
dateTime2 = now.strftime(', %H:%M:%S')

with open('MyLogHistory.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0

    for row in csv_reader:
        if line_count == 0: #if it's first line of csv.
            print(f'{", ".join(row)}')
            line_count += 1
            prev_date = '01/01/1980'
            prev_Active = '0'
            acc_H = acc_M = acc_S = 0

        curr_date = f'{row["Date"]}'

        #Separate Data per date.
        if curr_date > prev_date:
            if line_count > 1:
                print('Daily Total : ', acc_H, 'hours', acc_M, 'mins', acc_S, 'secs')
            prev_date = curr_date
            acc_H = acc_M = acc_S = 0
            print('-------------------------------')
        print(f'{row["Date"]} {row["Time"]} {row["EventID"]} {row["Event"]} {row["Active"]}')

        #Find and caulate Activated period.
        curr_Active = f'{row["Active"]}'
        if curr_Active != prev_Active:
            if f'{row["Active"]}' == '1':
                Active_start = f'{row["Time"]}'
                print("Start : ", Active_start)
                prev_Active = curr_Active
            elif f'{row["Active"]}' == '0':
                Active_end = f'{row["Time"]}'
                print("End : ", Active_end)
                prev_Active = curr_Active
                #Convert and separate H/M/S.
                Active_start_H = int(Active_start[0:2])
                Active_start_M = int(Active_start[3:5])
                Active_start_S = int(Active_start[6:8])

                Active_end_H = int(Active_end[0:2])
                Active_end_M = int(Active_end[3:5])
                Active_end_S = int(Active_end[6:8])

                #calculate delta.
                Delta_H = Active_end_H - Active_start_H
                Delta_M = Active_end_M - Active_start_M
                Delta_S = Active_end_S - Active_start_S

                if Delta_S < 0:
                    Delta_S += 60
                    Delta_M -= 1
                if Delta_M < 0:
                    Delta_M += 60
                    Delta_H -= 1

                print('Working time : ', Delta_H, Delta_M, Delta_S)

                #Accumulate daily total.
                acc_S += Delta_S
                if acc_S >= 60:
                    acc_M +=1
                    acc_S %= 60
                acc_M += Delta_M
                if acc_M >= 60:
                    acc_H += 1
                    acc_M %= 60

                acc_H += Delta_H

            else :
                print("Error!")
                prev_Active = '0'
        line_count += 1
    print(f'Processed {line_count} lines.')

    
#a = input("Input date :")
#b = input("Input date :")
#print('A = ', a)
#print('B = ', b)

#if a == b :
#    print("same date")
#elif a < b :
#    print("A is earlier than B")
#elif a > b :
#    print("B is earlier than A")
#else :
#    print("Error")

#print('A - B = ', a-b)
