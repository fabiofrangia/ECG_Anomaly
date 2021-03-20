import json 
import numpy as np
import os 
import random
import tqdm 
import scipy.io as sio

STEP = 256 

def load_ecg_mat(ecg_file):
    return sio.loadmat(ecg_file)['val'].squeeze()

def load_all(data_path):
    label_file = os.path.join(data_path, "REFERENCE-v3.csv")
    with open(label_file, 'r') as fid:
        records = [l.strip().split(",") for l in fid]

        dataset = []
        for record, label in tqdm.tqdm(records):
            ecg_file = os.path.join(data_path, "training2017/" + record + ".mat")
            ecg_file = os.path.abspath(ecg_file)
            ecg = load_ecg_mat(ecg_file)
            num_labels = ecg.shape[0] / STEP
            dataset.append((ecg_file, [label]*int(num_labels)))
        return dataset

def split(dataset, dev_frac):
    dev_cut = int(dev_frac * len(dataset))
    random.shuffle(dataset)
    dev = dataset[:dev_cut]
    train = dataset[dev_cut:]
    return train, dev

def make_json(save_path, dataset):
    with open(save_path, "w") as fid:
        for d in dataset:
            datum = {'ecg' : d[0],
                     'lables' : d[1]}
            json.dump(datum, fid)
            fid.write('\n')

if __name__ == "__main__":
    random.seed(2021)

    dev_frac = 0.1 
    data_path = "data"
    dataset = load_all(data_path)
    train, dev = split(dataset, dev_frac)
    make_json("data/train.json", train)
    make_json("data/dev.json", dev)