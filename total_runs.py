import csv
import matplotlib.pyplot as plt

def calculate(delivery_reader):
    """calculate data"""
    runs_by_teams = {}

    for deliveries in delivery_reader:
        team = deliveries['batting_team']
        total_runs = int(deliveries['total_runs'])

        runs_by_teams[team] = runs_by_teams.get(team, 0) + total_runs

    return runs_by_teams

def plot(teams, runs):
    """ Plotting Data"""
    plt.bar(teams, runs, lw=0.5, color='r', alpha=0.5, label='Total Runs')
    plt.xlabel('Teams', fontsize=15)
    plt.ylabel('Runs', fontsize=15)
    plt.xticks(rotation=15)
    plt.title('Total Runs Scored By Teams')
    plt.legend()
    plt.show()

def execute():
    """ Reading data from csv file"""
    with open('deliveries.csv', 'r', encoding='utf-8') as delivery_data:
        delivery_reader = csv.DictReader(delivery_data)
        runs_by_teams = calculate(delivery_reader)

        teams = list(runs_by_teams.keys())
        runs = list(runs_by_teams.values())

        plot(teams, runs)

if __name__ == "__main__":
    execute()
