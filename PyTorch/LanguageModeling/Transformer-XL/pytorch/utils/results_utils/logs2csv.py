import argparse
import json
import re
from pathlib import Path

import pandas as pd


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input",
        help="Path to input logs file with experiment result"
    )
    args = parser.parse_args()
    return args 


def main():
    args = get_args()
    columns = (
        'epoch', 'step', 'batches', 'lr', 'ms/batch', 'tok/s', 'loss', 'ppl')
    types = (int, int, int, float, float, int, float, float)
    df = pd.DataFrame(columns=columns)
    numbers_pattern = re.compile(r'[0-9\.]+')
    input_path = Path(args.input)
    descr_path = input_path.parent / Path('descr.json')
    train_path = input_path.parent / Path('train.csv')
    valid_path = input_path.parent / Path('valid.csv')
    test_path = input_path.parent / Path('test.csv')
    train_df, valid_df, test_df = \
        pd.DataFrame(), pd.DataFrame(), pd.DataFrame()
    with input_path.open() as inp_f, descr_path.open('w') as descr_f:
        params_line = next(inp_f)[5:]
        json.dump(json.loads(params_line), descr_f, indent=2)
        for line_i, line in enumerate(inp_f, 1):
            line = line[5:]
            line_data = json.loads(line)
            if line_data['step']:
                line_data['step'] = line_data['step'][0]
            else:
                del line_data['step']
            if 'data' in line_data:
                data_field = line_data['data']
                del line_data['data']
                line_data.update(data_field)
            else:
                raise ValueError(
                    f"Line number {line_i} has wrong format. It does not have "
                    f"field 'data'. Line data: {line_data}")
            if 'test_loss' in line_data:
                test_df = test_df.append(line_data, ignore_index=True)
            elif 'valid_loss' in line_data:
                valid_df = valid_df.append(line_data, ignore_index=True)
            elif 'train_loss' in line_data:
                train_df = train_df.append(line_data, ignore_index=True)
            else:
                raise ValueError(
                    f"Line number {line_i} has wrong format. It has to have "
                    f"one of the fields 'train_loss', 'valid_loss', "
                    f"'test_loss'. Line data: {line_data}")
    train_df.to_csv(train_path)
    valid_df.to_csv(valid_path)
    test_df.to_csv(test_path)


if __name__ == '__main__':
    main()
