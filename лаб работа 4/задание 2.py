# TODO импортировать необходимые молули
import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data = []
    with open(INPUT_FILENAME, 'r') as input_f:
        csv_reader = csv.DictReader(input_f)
        for row in csv_reader:
            data.append(row)

            with open(OUTPUT_FILENAME, 'w') as output_f:
                json.dump(data, output_f, indent=4)




if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
