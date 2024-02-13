import csv
import matplotlib.pyplot as plt

def calculate(matches_reader):
    """ calculate """
    matches_won_by_team_per_year = {}

    for matches in matches_reader:
        season = matches['season']
        matches_win = matches['winner']
        
        key = (matches_win, season)
        matches_won_by_team_per_year[key] = matches_won_by_team_per_year.get(key, 0) + 1

    return matches_won_by_team_per_year

def plot(unique_teams, teams, years, counts):
    """ plotting """

    fig, ax = plt.subplots()
    counts_previous_team = [0] * len(teams)

    for i, team in enumerate(unique_teams):
        team_counts = [counts[j] if teams[j] == team else 0 for j in range(len(teams))]
        ax.bar(years, team_counts, label=team, alpha=0.3, bottom=None if i == 0 else counts_previous_team )

        # Save the counts for the current team to be used as the bottom for the next team
        counts_previous_team = [team_counts[j] + (counts_previous_team[j] if teams[j] == team else 0) for j in range(len(teams))]

    ax.set_xlabel('Year')
    ax.set_ylabel('Number of Matches Won') 
    ax.legend(title='Team')

    plt.title('Number of Matches Won by Each Team per Year')
    plt.show()

def execute():
    """ read data"""
    with open('matches.csv', encoding='utf-8') as matches_reader:
        matches = csv.DictReader(matches_reader)
        matches_won_by_team_per_year = calculate(matches)

        teams, years, counts = zip(*[(team, year, count) for (team, year), count in matches_won_by_team_per_year.items()])
        unique_teams = set(teams)

        plot(unique_teams, teams, years, counts)

if __name__ == "__main__":
    execute()
