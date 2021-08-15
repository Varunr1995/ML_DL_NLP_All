import numpy as np
import pandas as pd
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.optim as optim
import torch.utils.data
from torch.autograd import Variable

movies = pd.read_csv("G:/Education/Machine Learning/ML_CSV_FILES/Movies Dataset/movies.dat", sep = '::', encoding = 'latin-1')
users = pd.read_csv("G:/Education/Machine Learning/ML_CSV_FILES/Movies Dataset/users.dat", sep = '::', encoding = 'latin-1')
ratings = pd.read_csv("G:/Education/Machine Learning/ML_CSV_FILES/Movies Dataset/ratings.dat", sep = '::', encoding = 'latin-1')

training_set = pd.read_csv("G:/Education/Machine Learning/ML_CSV_FILES/Movies Dataset/ml-100k/u1.base", delimiter = '\t')