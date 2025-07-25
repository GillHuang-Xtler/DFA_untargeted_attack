from loguru import logger
import pathlib
import os
from federated_learning.arguments import Arguments
from federated_learning.datasets import CIFAR10Dataset
from federated_learning.datasets import CIFAR100Dataset
from federated_learning.datasets import FashionMNISTDataset
from federated_learning.datasets import MNISTDataset
from federated_learning.datasets import STL10Dataset
# from federated_learning.datasets import TRECDataset
from federated_learning.utils import generate_train_loader
# from federated_learning.utils import generate_benign_loader, generate_malicious_loader, generate_free_loader
from federated_learning.utils import generate_test_loader
from federated_learning.utils import save_data_loader_to_file


if __name__ == '__main__':
    args = Arguments(logger)

    dataset = FashionMNISTDataset(args)
    TRAIN_DATA_LOADER_FILE_PATH = "data_loaders/fashion-mnist/train_data_loader.pickle"
    TEST_DATA_LOADER_FILE_PATH = "data_loaders/fashion-mnist/test_data_loader.pickle"

    if not os.path.exists("data_loaders/fashion-mnist"):
        pathlib.Path("data_loaders/fashion-mnist").mkdir(parents=True, exist_ok=True)

    train_data_loader = generate_train_loader(args, dataset)
    test_data_loader = generate_test_loader(args, dataset)



    with open(TRAIN_DATA_LOADER_FILE_PATH, "wb") as f:
        save_data_loader_to_file(train_data_loader, f)

    with open(TEST_DATA_LOADER_FILE_PATH, "wb") as f:
        save_data_loader_to_file(test_data_loader, f)

