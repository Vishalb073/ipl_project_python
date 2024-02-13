import csv
import matplotlib.pyplot as plt

def calculate(deliveries_reader):
    """ calculate """
    top_batsman = {}

    for deliveries in deliveries_reader:
        if deliveries['batting_team'] == 'Royal Challengers Bengaluru':
            batsman = deliveries['batsman']
            runs = int(deliveries['batsman_runs'])
            top_batsman[batsman] = top_batsman.get(batsman, 0) + runs

    return top_batsman

def plot(players, runs):
    """ plotting bar"""
    plt.bar(players, runs, lw=0.5, alpha=0.5)
    plt.xlabel('Players', fontsize=15)
    plt.ylabel('Runs', fontsize=15)
    plt.title('Top 10 Batsmen of RCB', fontsize=15)
    plt.show()

def execute():
    """ Reading data from csv file"""
    with open('deliveries.csv', 'r', encoding='utf-8') as deliveries:
        batsman_reader = csv.DictReader(deliveries)
        top_batsman = calculate(batsman_reader)

        sorted_batsmen = sorted(top_batsman.items(), key=lambda x: x[1], reverse=True)
        top_ten_batsmen = sorted_batsmen[:10]
        players, runs = zip(*top_ten_batsmen)

        plot(players, runs)

if __name__ == "__main__":
    execute()
