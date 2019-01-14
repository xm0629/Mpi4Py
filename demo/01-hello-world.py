# -*-coding:utf-8-*-
# Project: hello-world
# Author: Ming Xu
# Data:   2019-01-14

from mpi4py import MPI

comm = MPI.COMM_WORLD
print("Hello! I'm rank %d from %d running in total..." % (comm.rank, comm.size)) # 0 rank, and total 1 rank
comm.Barrier()







