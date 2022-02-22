import json
from collections import defaultdict


def printscore(path):
    with open(path, "r") as fh:
        json_obj = json.load(fh)
        print(f"班級：{json_obj['class']}")
        result = defaultdict(list)

        for i in json_obj['score']:
            for j, k in i.items():
                result[j].append(k)

        for j, k in result.items():
            print(f'科目：{j}')
            print(f'\t最低分：{max(k)}')
            print(f'\t最高分：{min(k)}')
            print(f'\t平均：{sum(k) / len(k)}')


