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

