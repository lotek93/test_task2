1) build:

docker build -t test/test . 


2) run container:

docker run -ti --name test test/test


3) run unittest:

python3 -m unittest -v utest_testwork.py


4) run program for help:

python3 testwork.py -h 


5) run program for demo:

python3 testwork.py -d