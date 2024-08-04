"""Задача 4. Турнир"""


def count_players_score_tour():
    """count_players_score_tour
    """
    with open("Module22/04_tournament/first_tour.txt",
              "r", encoding="utf8") as f:
        list_name = []
        data = []
        list_score = []
        content = f.readlines()
        for step in content:
            data.append(step.split())
        for step in data:
            save = ''
            score = 0
            for step2 in step:
                if score == 0:
                    save = step2[0] + '. '
                    score += 1
                elif score == 1:
                    save += step2
                    score += 1
                else:
                    list_score.append(int(step2))
                    list_name.append(save)

        with open("second_tour_task_4.txt", "w+",
                  encoding="utf8") as f:
            content = {}
            score = 0
            length = len(list_score)
            for step in range(length):
                if list_score[step] >= 90:
                    content[list_name[step]] = list_score[step]
            sorted_content = dict(
                sorted(content.items(), key=lambda
                       item: item[1], reverse=True))
            f.write(f'{len(content)}\n')
            for step in sorted_content:
                score += 1
                f.write(f'{score}) {step} {sorted_content[step]}\n')
            f.seek(0)
            text = f.read()
            print(text)


def main():
    """main function
    """
    count_players_score_tour()


main()
