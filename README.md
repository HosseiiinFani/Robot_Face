# How to run:

to run the program, you first have to create a virtual environment and install the required packages.

## MacOS/Linux
```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Windows
```
py -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

then use `python main.py` or `py main.py` to run the code.

# Connecting to arduino

if you want to use the output from an arduino serial monitor to change the mood, simply change the `PORT` variable in the `main.py` file to the port your arduino is connected to.

```py
...
PORT="YOUR_PORT"
...
```

if you dont, you can use the on screen buttons to interact with the program.

# How to monitor RAM usage

to see how much ram the program takes up, simply run the following command while the program is running:

```
$ ps -m -o %cpu,%mem,command 
27.0  0.2 python main.py
```

the output contains the cpu percentage used, memory percentage used and the command name.