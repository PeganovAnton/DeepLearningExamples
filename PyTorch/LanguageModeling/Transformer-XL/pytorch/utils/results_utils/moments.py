import argparse

import pandas as pd


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_files",
        nargs="+",
        help="Paths to csv files with results"
    )
    parser.add_argument(
        "--row_index",
        "-r",
        type=int,
        help="Index of a row which will be taken for moments computation"
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Path to output csv file"
    )
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    aggregated = pd.DataFrame()
    for f in args.input_files:
        df = pd.read_csv(f)
        aggregated = aggregated.append(df.iloc[[args.row_index]])
    aggregated = aggregated.select_dtypes(include=["number"])
    mean = aggregated.mean(axis=0)
    std = aggregated.std(axis=0, ddof=1)
    moments_df = pd.DataFrame({"mean": mean, "std": std})
    moments_df.to_csv(args.output)


if __name__ == '__main__':
    main()
