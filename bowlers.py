import csv
import matplotlib.pyplot as plt

def calculate(match_reader):
    """ calculate """
    economy_bowlers = {}

    for matches in match_reader:
        if 'match_id' in matches and 518 <= int(matches['match_id']) <= 576:
            bowler = matches['bowler']
            runs_by_bowler = int(matches['total_runs'])
            balls_by_bowler = int(matches['ball'])

            if bowler in economy_bowlers:
                economy_bowlers[bowler]['runs'] += runs_by_bowler
                economy_bowlers[bowler]['balls'] += balls_by_bowler
            else:
                economy_bowlers[bowler] = {'runs': runs_by_bowler, 'balls': balls_by_bowler}

    for bowler in economy_bowlers:
        runs = economy_bowlers[bowler]['runs']
        balls = economy_bowlers[bowler]['balls']
        economy_rate = (runs / (balls / 6)) * 6  
        economy_bowlers[bowler]['economy_rate'] = economy_rate

    sorted_bowlers = sorted(economy_bowlers.items(), key=lambda x: x[1]['economy_rate'], reverse=False)      
    top_ten_bowlers_by_eco = sorted_bowlers[:10]

    return top_ten_bowlers_by_eco

def plot(bowlers, economy_rates):
    """plotting bar"""
    # Plot the bar chart
    plt.bar(bowlers, economy_rates, color='skyblue')
    plt.xlabel('Bowler')
    plt.ylabel('Economy Rate')
    plt.title('Top 10 Economical Bowlers in 2015')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def execute(): 
    """read data"""
    with open('deliveries.csv', encoding='utf-8') as reader:
        match_reader = csv.DictReader(reader)
        top_ten_bowlers_by_eco = calculate(match_reader)

        bowlers = [b[0] for b in top_ten_bowlers_by_eco]
        economy_rates = [b[1]['economy_rate'] for b in top_ten_bowlers_by_eco]

        plot(bowlers, economy_rates)

if __name__ == "__main__":
    execute()
