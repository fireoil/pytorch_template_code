import os
from IPython.display import display
import matplotlib.pyplot as plt
import visdom
from graphviz import Digraph
import time
%matplotlib inline

from torch.utils.data import Dataset, DataLoader
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as T

import numpy as np
import pandas as pd
from tqdm import tqdm_notebook as tqdm
import PIL
from PIL import Image
import cv2

from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import roc_curve

!ls ../input