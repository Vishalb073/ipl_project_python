
import csv
import matplotlib.pyplot as plt

def calculate(matches_reader):
    """"calculate"""
    matches_counter = {}

    for season in matches_reader:
        matches_counter[season['season']] = matches_counter.get(season['season'], 0) + 1

    return matches_counter

def plot(sorted_years, sorted_count):
    """plotting"""
    plt.bar(sorted_years, sorted_count, lw=0.5, alpha=0.5, label='Matches count per season', color='red')
    plt.xlabel('Years', fontsize=15)
    plt.ylabel('Matches Played', fontsize=15)
    plt.title('Matches Played by Season')
    plt.legend()
    plt.show()

def execute():
    """"execution"""
    with open('matches.csv', encoding= 'utf-8') as matches_reader:
        matches_played = csv.DictReader(matches_reader)
        matches_counter = calculate(matches_played)

        sorted_years = sorted(matches_counter.keys())
        sorted_count = [matches_counter[year] for year in sorted_years]

        plot(sorted_years, sorted_count)

if __name__ == "__main__":
    execute()
