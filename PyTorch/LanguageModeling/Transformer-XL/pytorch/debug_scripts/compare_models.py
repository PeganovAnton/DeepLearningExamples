import sys
sys.path += ['/home/apeganov/DeepLearningExamples/PyTorch/LanguageModeling/Transformer-XL/pytorch']

import os
print("cwd:", os.getcwd())

from mem_transformer import *
import numpy as np
import pickle
import torch


def compare_models():
    tpath = 'debug_models/train_model.pickle'
    epath = 'debug_models/eval_model.pickle'
    with open(tpath, 'rb') as tf, open(epath, 'rb') as ef:
        train_model = pickle.load(tf)
        eval_model = pickle.load(ef)
    for k in train_model.__dict__.keys():
        tv = getattr(train_model, k)
        ev = getattr(eval_model, k)
        if isinstance(tv, np.ndarray):
            if (tv != ev).any():
                print(k, ev, tv)
        elif isinstance(tv, torch.Tensor):
            if (tv != ev).any():
                print(k, tv, ev)
        elif isinstance(tv, dict):
            for kk in tv:
                if isinstance(tv[kk], np.ndarray):
                    if (tv[kk] != ev[kk]).any():
                        print(k, tv, ev)
                        break
                elif isinstance(tv[kk], torch.Tensor):
                    if (tv[kk] != ev[kk]).any():
                        print(k, tv, ev)
                        break
                else:
                    if tv[kk] != ev[kk]:
                        print(k, tv, ev)
                        break
        else:
            if tv != ev:
                print(k, tv, ev)


if __name__ == '__main__':
    compare_models()
