import os
# Works but causes issues since filepath is relative to the file the module is called in
#from ..my_classes.game_class import Game


work_dir = os.getcwd()


def pwd():
    return work_dir


def num_cpus():
    return os.cpu_count()


def return_new_vegas():
    return None
    # return Game("Fallout New Vegas","PC",100)