import argparse
from pathlib import Path

import numpy as np
from matplotlib import pyplot as plt


def get_attn(path):
    path = path.expanduser()
    attn_path = path / Path('attn.npy')
    keys_path = path / Path('keys.npy')
    queries_path = path / Path('queries.npy')
    with attn_path.open('rb') as af, keys_path.open('rb') as kf, queries_path.open('rb') as qf:
        return {'attn': np.load(af), 'keys': np.load(kf), 'queries': np.load(qf)}


def plot_attention_weights(attentions, queries, keys, layer, filename=Path('att.png'), save=False, show=False):
    filename = filename.expanduser()
    filename.parent.mkdir(parents=True, exist_ok=True)
    # attentions n_layers x n_heads x len x len
    fig = plt.figure(figsize=(90, 270))

    attention = attentions[layer]

    for head in range(attention.shape[0]):
        ax = fig.add_subplot(6, 2, head + 1)

        # plot the attention weights
        ax.matshow(attention[head][:len(queries), :len(keys)], cmap='Reds')

        fontdict = {'fontsize': 11}

        ax.set_xticks(range(len(keys)))
        ax.set_yticks(range(len(queries)))

        ax.set_xticklabels(keys, fontdict=fontdict, rotation=90)

        ax.set_yticklabels(queries, fontdict)

        ax.set_xlabel('Head {}'.format(head + 1), fontdict)

    plt.tight_layout()
    if save:
        plt.savefig(filename)
    if show:
        plt.show()


def plot_all_attention_maps(data_path, save_path, batch_elem_idx, steps):
    for step in steps:
        data = get_attn(data_path / Path(f'step{step}'))
        sh = data['attn'].shape
        for li in range(sh[0]):
            plot_attention_weights(
                data['attn'][:, batch_elem_idx, ...],
                data['queries'][batch_elem_idx],
                data['keys'][batch_elem_idx],
                li,
                filename=save_path / Path(f'step_{step}/layer_{li}.png'),
                save=True
            )


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "data_path",
        type=Path,
        help="Path to dir with directories 'step1', 'step2' and so on, each which"
             "in turn contain files 'attn.npy', 'queries.npy', 'keys.npy'."
    )
    parser.add_argument(
        "save_path",
        type=Path,
        help="Path to directory where plots will be saved."
    )
    parser.add_argument(
        "--batch_elem_idx",
        type=int,
        help="Element of the batch which will be plotted. Default is 0.",
        default=0
    )
    parser.add_argument(
        "--steps",
        nargs="+",
        type=int,
        help="List of indices of steps which will be plotted.",
        default=[1, 2, 3, 4, 5, 6]
    )
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    plot_all_attention_maps(args.data_path, args.save_path, args.batch_elem_idx, args.steps)


if __name__ == '__main__':
    main()
