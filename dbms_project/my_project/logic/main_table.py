import csv
import random
x = 3000;


with open('student_data_file.csv', mode='w') as data_file:
    student_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    student_writer.writerow(['ROLLNO', 'NAME', 'DOB','GENDER', 'PCM_PERCENTAGE', 'CGPA',])

    for i in range (0, 1000):
        x = x + 1
        dob = ''
        date = random.randint(1, 28)
        month = random.randint(1, 12)
        year = random.randint(2002, 2003)
        if date < 10 and month >= 10 :
            dob = f'0{date}{month}{year}'
        
        elif month < 10 and date < 10:
            dob = f'0{date}0{month}{year}'

        elif month <10 and date >= 10:
            dob = f'{date}0{month}{year}'
        
        elif month>=10 and date >=10:
            dob = f'{date}{month}{year}'
        
        dateofbirth = str(dob) 

        student_writer.writerow([f'10210{x}', 'NAME', f'{dateofbirth}','gender', f'{random.randint(70, 100)}', f'{random.randint(500, 1000)/100}',])