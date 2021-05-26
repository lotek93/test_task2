There is a xml file with structure describing date and time of employee arrival and departure:

&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;
&lt;people&gt;
&lt;person full_name=&quot;i.ivanov&quot;&gt;
&lt;start&gt;21-12-2011 10:54:47&lt;/start&gt;
&lt;end&gt;21-12-2011 19:43:02&lt;/end&gt;
&lt;/person&gt;
&lt;person full_name=&quot;a.stepanova&quot;&gt;
&lt;start&gt;21-12-2011 09:40:10&lt;/start&gt;
&lt;end&gt;21-12-2011 17:59:15&lt;/end&gt;
&lt;/person&gt;
...
&lt;/people&gt;

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
