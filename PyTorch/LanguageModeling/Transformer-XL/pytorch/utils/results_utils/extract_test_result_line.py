import argparse
import glob
import re

import pandas as pd


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--files",
        nargs="+",
        help="List of csv files from which data is taken"
    )
    parser.add_argument(
        "--file_var_regex",
        help="Regex to extract variable from file name. Group 1 has to "
             "contain the variable."
    )
    parser.add_argument(
        "--file_var_name",
        help="Name of a variable extracted from file names"
    )
    parser.add_argument(
        "--file_var_type",
        type=eval,
        help="The type of variable extracted from file names. "
             "Default is `int`",
        default=int,
    )
    parser.add_argument(
        "--cols",
        nargs="+",
        help="Names of columns in csv files frow which values will be added to"
             "resulting table. By default all columns are used."
    )
    parser.add_argument(
        "--row_index",
        type=int,
        help="Index of a row from which values of columns `cols` will be taken"
    )
    parser.add_argument(
        "--sort_column",
        help="Name of a column by which elements are sorted in non descending "
             "order."
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Path to output_csv file."
    )
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    file_var_pattern = re.compile(args.file_var_regex)
    if args.cols is None:
        first_df = pd.read_csv(args.files[0])
        col_names = list(first_df.columns)
    else:
        col_names = args.cols
    result_col_names = [args.file_var_name] + col_names
    result = pd.DataFrame(columns=result_col_names)
    for f in args.files:
        m = file_var_pattern.search(f)
        if m is None:
            raise ValueError(
                f"File '{f}' does not match regex '{args.file_var_regex}'")
        file_data = {args.file_var_name: args.file_var_type(m.group(1))}
        f_df = pd.read_csv(f)
        for col in col_names:
            file_data[col] = f_df.iloc[args.row_index].loc[col]
        result = result.append([file_data], ignore_index=True)
    result = result.sort_values(by=[args.sort_column])
    result.to_csv(args.output)


if __name__ == '__main__':
    main()
