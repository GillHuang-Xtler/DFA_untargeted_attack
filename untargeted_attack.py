from federated_learning.utils import default_no_change
from federated_learning.worker_selection import RandomSelectionStrategy
from federated_learning.server import run_exp

if __name__ == '__main__':

    START_EXP_IDX = 202501
    NUM_EXP = 1
    REPLACEMENT_METHOD = default_no_change
    KWARGS = {
        "NUM_WORKERS_PER_ROUND" : 10
    }

    for experiment_id in range(START_EXP_IDX, START_EXP_IDX + NUM_EXP):
        run_exp(REPLACEMENT_METHOD, 0, KWARGS, RandomSelectionStrategy(), experiment_id)
