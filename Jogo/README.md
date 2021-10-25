# Installation Summary
1. Install Miniconda 3
2. Install Kivy
3. Clone This Repository
4. Testing Installation

## 1. Install Miniconda 3
Follow the instructions on the following [link](https://docs.conda.io/en/latest/miniconda.html)

## 2. Install Kivy
With Miniconda 3 installed, using anaconda powershell (on Windows)
1. Create an environment and name it as you wish.

`conda create --name tcc python=3.6` 

2. Activate the environment

`conda activate tcc`

3. You can follow the instructions on the [link](https://kivy.org/doc/stable/gettingstarted/installation.html), or simply use the commands below:

`python -m pip install --upgrade pip setuptools virtualenv`

`python -m pip install kivy[full] kivy_examples`

## 3.Clone This Repository
For organization purposes, create an workspace directory inside your environment and clone this repository in it
`mkdir workspace`
 
 If not installed on your machine, install using the [link](https://git-scm.com/download/win) and then:
 `git clone https://github.com/isamaues/TCC.git`

## 4.Testing Installation
run main.py on the tcc environment on miniconda:

`python main.py`
