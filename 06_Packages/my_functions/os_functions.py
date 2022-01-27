import os

work_dir = os.getcwd()


def pwd():
    return work_dir


def num_cpus():
    return os.cpu_count()