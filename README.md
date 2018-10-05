# homework1 on Numerical Analysis using PyThon
homework1 on Numerical Analysis using PyThon
* Vending Machine
* Weired Dictionary
## Requirements

* 필수
```
sudo pip3 install requirements.txt
```
* Vendig Machin Gui에 필요한 Package
```
sudo apt-get install python3-pyqt5
sudo apt-get install python3-pyqt5.qtsql
sudo apt-get install qttools5-dev-tools
```
* Python Package 등록
```
echo 'export PYTHONPATH=<Your Project Path>/:${PYTHONPATH}' >> ~/.bashrc
```
## Usage
* Vending Machine
```
cd vending_machine && python3 main.py
```
* Vending Machine Using Qt GUI(Not Complete)
```
cd vending_machine && python3 main_window.py
```
* Weired Dictionary
```
cd weired_dictionary && python3 main.py
```

## Configuration
각 폴더의 config.cfg의 옵션 사용

* 참고
```
[DEFAULT]
path = /home/kist/coursework/homework1_NA/vending_machine
filename = Beverage.csv
filepath = /home/kist/coursework/homework1_NA/vending_machine/Beverage.csv
init_df = 1
```