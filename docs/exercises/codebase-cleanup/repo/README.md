
# Rock Paper Scissors Game

This repo provides an example of reorganizing code, and importing code from one file to another.

We start with a working implementation of a command line game of rock paper scissors, in "app/rps_starter.py". This file is separate just for reference purposes.

We copy this code into "app/rps.py" and refactor using an iterative approach.

After the code is refactored, we extend the functionality by creating a web application interface in "app/rps_web.py", which imports code from the original file.

## Setup

Create and activate virtual environment:

```sh
conda create -n rps-env python=3.11
conda activate rps-env
```

Install package(s):

```sh
#pip install flask

pip install -r requirements.txt
```


## Usage

Run the command line app:

```sh
#python app/rps.py

python -m app.rps

```


Run the web app:

```sh
python -m app.rps_web
```
