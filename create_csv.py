import csv


def create_example_students_csv(path_to_csv):
    # 14 lectures (4 hours each ) = 3360 minutes
    header = ['name', 'total time', 'total percentage', 'number of meetings']
    data = [['Michal', '2485', '74 %', '14'], ['Jeff', '2199', '65 %', '13']]

    with open(path_to_csv, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(data)

def read_from_csv(path_to_csv, mysql):
    csvfile = open(path_to_csv, newline='')
    # make a new variable - c - for Python's DictReader object
    c = csv.DictReader(csvfile)
    # read from DictReader object
    # using the column headings from the CSV as the dict keys
    #for row in c:
    #    print(row['name'] + row['total time'] + row['total percentage'] + row['number of meetings'])

    for row in c:
        sql = " INSERT INTO `flaskdb`.`Attendance`(`name`, `total time`, `total percentage`, `num of meetings`) VALUES (%s, %s, %s, %s)"
        values = (row['name'], row['total time'], row['total percentage'], row['number of meetings'])
        print(row['name'] +"\t"+ row['total time'] +"\t"+ row['total percentage'] +"\t"+ row['number of meetings'])
        mysql.connection.cursor().execute(sql, values)
        mysql.connection.commit()

    # save and close the file
    csvfile.close()

    
