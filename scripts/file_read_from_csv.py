from csv import Sniffer, DictReader

file_name = 'people_data.csv'
with open(file_name, 'rb') as csv_file:
    dialect = Sniffer().sniff(csv_file.read(1024))
    csv_file.seek(0)
    sum = 0.0
    csv_reader = DictReader(csv_file, fieldnames=None,
                                restkey='rest', restval=None,
                                dialect=dialect)
    for row in csv_reader:
        print('{name} --- {weight}'.format(name=row['name'],
                                           weight=row['weight']))
        sum += float(row['weight'])
    print('sum = {0}'.format(sum))
