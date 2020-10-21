import argparse
import datetime as dt
import xml.etree.ElementTree as ET


def count_hours(filename, by_employee=False, start_date='', end_date=''):
    counts = {}
    start_date = dt.date.min if start_date == '' else dt.datetime.strptime(start_date, '%d-%m-%Y').date()
    end_date = dt.date.max if end_date == '' else dt.datetime.strptime(end_date + ' 23:59:59', '%d-%m-%Y %H:%M:%S').date()

    root = ET.parse(filename).getroot()
    for level1 in root:
        if level1.tag == 'person':
            employee = level1.attrib['full_name']
            start = ''
            end = ''
            for level2 in level1:
                if level2.tag == 'start':
                    start = dt.datetime.strptime(level2.text, '%d-%m-%Y %H:%M:%S')
                elif level2.tag == 'end':
                    end = dt.datetime.strptime(level2.text, '%d-%m-%Y %H:%M:%S')
            date = dt.datetime.strftime(start, '%d-%m-%Y')

            if start_date <= start.date() <= end_date:
                if by_employee:
                    if date not in counts.keys():
                        counts[date] = {employee: dt.timedelta(0)}
                    else:
                        if employee not in counts[date].keys():
                            counts[date][employee] = dt.timedelta(0)
                    counts[date][employee] = end - start + counts[date][employee]
                else:
                    if date not in counts.keys():
                        counts[date] = dt.timedelta(0)
                    counts[date] = end - start + counts[date]

    return counts


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Accounting total hours from special xml file.')
    parser.add_argument('-d', action='store_true', dest='demos', help='run demos')
    parser.add_argument('-f', action='store', dest='fname', help='xml file name')
    parser.add_argument('-e', action='store_true', dest='employee', help='group hours by employees')
    parser.add_argument('-start', action='store', dest='start', help='start date in format DD-MM-YYY')
    parser.add_argument('-end', action='store', dest='end', help='end date in format DD-MM-YYY')
    args = parser.parse_args()

    if args.demos:
        print('Running demos:\n')
        hours = count_hours('test.xml')
        print(f'demo 1: base run. response: {hours}\n')

        hours = count_hours('test.xml', by_employee=True)
        print(f'demo 2: group hours by employees. response: {hours}\n')

        hours = count_hours('test.xml', by_employee=True, start_date='22-12-2011', end_date='22-12-2011')
        print(f'demo 3: group hours by employees within dates range. response: {hours}\n')

    elif args.fname is not None:
        start = args.start if args.start is not None else ''
        end = args.end if args.end is not None else ''
        hours = count_hours(args.fname, args.employee, start, end)
        print(hours)

    else:
        parser.print_usage()
