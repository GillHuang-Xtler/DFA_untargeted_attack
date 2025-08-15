## DFA_untargeted_attack

Code repository for paper "Fabricated Flips: Poisoning Federated Learning without Data", DSN2023.
The example dataset is FashionMNIST, the downloading and default model settings are already set in the files, you do not need to prepare by yourself.

# To run this file

- python version in the development environment:3.8.10
- pip install -r requirements.txt
- python generate_data_distribution.py
- python generate_default_models.py
- python untargeted_attack.py

# Note
- arguments are in 'federated_learning/arguments.py' + untargeted_attack.py
- set a START_EXP_IDX in untargeted_attack.py and python untargeted_attack.py
- the logs/results data will be in the logs/res folder

### Configuration
In arguments.py

- self.attack = "none" # no attacks

- self.attack = "cua" # the attack method of the paper
