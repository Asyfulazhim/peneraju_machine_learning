import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings("ignore")

#Fill your code hereimport matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import warnings
warnings.filterwarnings("ignore")

num = int(input("Enter the number of features\n"))

print("Enter the features in comma separated format")
for i in range(num):
    feature = input().split(',')