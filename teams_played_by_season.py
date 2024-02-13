import csv
import matplotlib.pyplot as plt


def calculate(matches_reader):
    """ calculate """
    games_count = {}

    for games in matches_reader:
        team1 = games['team1']
        team2 = games['team2']
        season = games['season']

        games_count[(team1, season)] = games_count.get((team1, season), 0) + 1
        games_count[(team2, season)] = games_count.get((team2, season), 0) + 1


    return games_count

def plot(games):

    """ plotting"""
    teams, season = zip(*(games.items()))
    teams, season = zip(*teams) 
    count = list(games.values())
    unique_teams = set(teams)
    season = list(season)

    fig, ax = plt.subplots()
    bottom_count = [0] *len(unique_teams)
    team_colors = ['blue', 'green', 'red', 'purple', 'orange', 'brown', 'pink', 'gray', 'olive', 'cyan', 'indigo', 'magenta', 'yellow', 'teal']
    
    for i, team in enumerate(unique_teams):
        team_counts = [count[j] if teams[j] == team else 0 for j in range(len(teams))]
        ax.bar(season, team_counts, label=team ,color = team_colors[i], alpha = 0.2,bottom = None if i == 0 else bottom_count)

        bottom_count = [team_counts[j] + (bottom_count[j] if j < len(bottom_count) else 0) for j in range(len(team_counts))]
        # ax.bar(season, teams , team_counts , bottom =count)
       # counts = [ x + y for x , y in zip(bottom , team_counts)]
       # ax.bar(season, bottom, label=team, bottom=cumulative_counts[:-1], alpha=0.2) 
    
    ax.set_xlabel('Season')
    ax.set_ylabel('Number of Games Played')
    ax.legend(title='Team', bbox_to_anchor=(1, 1), loc='upper left')

    plt.title('Number of Games Played by Each Team per Season')
    plt.xticks(rotation=45, ha='right') 
    plt.tight_layout()
    plt.show()

def execute():
    """ read data"""
    with open('matches.csv', encoding='utf-8') as games:
        matches_reader = csv.DictReader(games)
        games = calculate(matches_reader)

        
        plot(games)

if __name__ == "__main__":
    execute()



