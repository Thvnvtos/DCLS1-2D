from typing import Callable, Optional

import numpy as np

from torch.utils.data import DataLoader
from spikingjelly.datasets import pad_sequence_collate

from spikingjelly.datasets.shd import SpikingHeidelbergDigits

from utils import set_seed


'''
We don't need the modified binning version in this project.
'''

def SHD_dataloaders(config):
  set_seed(config.seed)

  train_dataset = SpikingHeidelbergDigits(config.datasets_path, train=True, data_type='frame', duration=config.time_step)
  test_dataset= SpikingHeidelbergDigits(config.datasets_path, train=False, data_type='frame', duration=config.time_step)

  train_loader = DataLoader(train_dataset, collate_fn=pad_sequence_collate, batch_size=config.batch_size, shuffle=True, num_workers=4)
  test_loader = DataLoader(test_dataset, collate_fn=pad_sequence_collate, batch_size=config.batch_size, num_workers=4)

  return train_loader, test_loader