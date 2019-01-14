# -*-coding:utf-8-*-
# Project: broadcast
# Author: Ming Xu
# Data:   2019-01-14

import numpy as np
from mpi4py import MPI


comm = MPI.COMM_WORLD


comm.Barrier()

N = 5
if comm.rank == 0:
    A = np.arange(N, dtype=np.float64)    # rank 0 has proper data
else:
    A = np.empty(N, dtype=np.float64)     # all other just an empty array

comm.Bcast([A, MPI.DOUBLE])

print("[%02d] %s" % (comm.rank, A))