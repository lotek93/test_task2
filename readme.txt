There is a xml file with following structure describing date and time of employee arrival and departure:

<?xml version="1.0" encoding="UTF-8"?>
<people>
<person full_name="i.ivanov">
<start>21-12-2011 10:54:47</start>
<end>21-12-2011 19:43:02</end>
</person>
<person full_name="a.stepanova">
<start>21-12-2011 09:40:10</start>
<end>21-12-2011 17:59:15</end>
</person>
...
</people>

The task is to write a python program that calculates total time of employees presence for each day.


Solution:

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
