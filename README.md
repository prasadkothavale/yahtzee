# yahtzee
I recently learned about Yahtzee dice game which I think is more probability based. Hence wanted to analyze probabilities of each scenario and try to train a bot using neural networks and one bot using probabilities and observer their performance

### Create venv
```sh
python -m venv env
```

### Activate venv
```sh
source env/bin/activate
```

### Install dependencies
```sh
pip3 install tabulate
```

### Start game in command line mode
```sh
python core/game_cli.py --players=2
```

### Running tests
```sh
python -m unittest discover tests
```
