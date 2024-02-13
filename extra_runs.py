import csv
import matplotlib.pyplot as plt

def calculate(extra_runs_dict, start_match_id, end_match_id):
    """ calculate """
    with open('deliveries.csv', encoding='utf-8') as reader:
        count_runs = csv.DictReader(reader)

        for runs in count_runs:
            if 'match_id' in runs and start_match_id <= int(runs['match_id']) <= end_match_id:
                team = runs['bowling_team']
                runs = int(runs['extra_runs'])
                extra_runs_dict[team] = extra_runs_dict.get(team, 0) + runs

    return extra_runs_dict

def plot(extra_runs_dict):
    """plotting """ 
    plt.bar(extra_runs_dict.keys(), extra_runs_dict.values(), lw=0.5, alpha=0.5, color='green')
    plt.xlabel('Teams', fontsize=15)
    plt.ylabel('Extra_runs', fontsize=15)
    plt.title('Extra runs in 2016')
    plt.legend()
    plt.show()

def execute():
    """"execute both functions"""
    start_match_id = 577
    end_match_id = 636
    extra_runs_dict = {}

    extra_runs_dict = calculate(extra_runs_dict, start_match_id, end_match_id)
    plot(extra_runs_dict)

if __name__ == "__main__":
    execute()
