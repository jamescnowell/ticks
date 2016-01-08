import argparse
import requests
import csv
import StringIO
from tabulate import tabulate


def parse_args():
    parser = argparse.ArgumentParser(description='Shows info for the passed ticker names')
    parser.add_argument('input', action='store', type=str, nargs='+',
                        help='the input file to be converted to LaTeX and PDF')
    args = parser.parse_args()
    return args


def main():
    args = parse_args()
    syms = ','.join(args.input)
    r = requests.get('http://download.finance.yahoo.com/d/quotes.csv?s=%s&f=nsl1oc1p2' % syms)
    clean = r.text
    syms = []
    reader = csv.reader(StringIO.StringIO(clean), delimiter=",", quotechar='"')
    for row in reader:
        syms.append(row)
    print(tabulate(syms, headers=['Name', 'Symbol', 'Price', 'Open', 'Change', 'Change%'], floatfmt=".2f"))

if __name__ == '__main__':
    main()
