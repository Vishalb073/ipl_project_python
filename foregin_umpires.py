import csv
import matplotlib.pyplot as plt

def calculate(umpires_reader):
    """ calculate """
    umpires_count = {}

    for umpires in umpires_reader:
        country = umpires['country'].strip()

        if country != 'India':
            umpires_count[country] = umpires_count.get(country, 0) + 1

    return umpires_count

def plot(countries, count):
    """ plotting """
    plt.bar(countries, count, lw=0.8, color='black', alpha=0.5)
    plt.xlabel('Country', fontsize=15)
    plt.ylabel('Counts', fontsize=15)
    plt.title('Umpires Country Count', fontsize=15)
    plt.show()

def execute():
    """read data"""
    with open('umpires.csv', 'r', encoding='utf-8') as umpire:
        umpires_reader = csv.DictReader(umpire)
        umpires_count = calculate(umpires_reader)

        countries = list(umpires_count.keys())
        count = list(umpires_count.values())

        plot(countries, count)

if __name__ == "__main__":
    execute()
