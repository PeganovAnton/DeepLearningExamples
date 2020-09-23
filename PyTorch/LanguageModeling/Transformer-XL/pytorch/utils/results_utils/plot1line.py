import argparse
import json

import pandas as pd
import seaborn as sns


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input",
        help="Path to input csv file"
    )
    parser.add_argument(
        "output",
        help="Path to output png file"
    )
    parser.add_argument(
        "config",
        help="Path to config json file"
    )
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    df = pd.read_csv(args.input)
    with open(args.config) as f:
        config = json.load(f)
    plot_axes = sns.lineplot(
        x=config['x'],
        y=config['y'],
        data=df,
    )
    plot_axes.set_xlabel(config['xlabel'])
    plot_axes.set_ylabel(config['ylabel'])
    plot_axes.set_xscale(config.get('xscale', 'linear'))
    plot_axes.set_yscale(config.get('yscale', 'linear'))
    plot_axes.grid(config.get('grid'))
    plot_axes.figure.savefig(args.output)


if __name__ == '__main__':
    main()

