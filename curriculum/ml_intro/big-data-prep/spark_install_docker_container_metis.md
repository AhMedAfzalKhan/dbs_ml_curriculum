# Installing Spark on AWS

Go to http://aws.amazon.com and start one of your instances, if it hasn't already started.

Copy down your IP address. This notebook will use `xxx.xxx.xxx.xxx` in place of your instance


## Log onto AWS and set up directories (local and AWS steps)

1. Log on to your AWS EC2 instance. 
```bash
ssh -i ~/.ssh/aws_key.pem ubuntu@xxx.xxx.xxx.xxx
```
Do this step on your local machine

2. From your AWS terminal, create a directory for our notebooks:
```bash
mkdir -p notebooks/data
```
We will be sharing the `notebooks` and `notebooks/data` directories between the regular `ubuntu` user and our Docker container.

## Get a Spark container (all run on AWS)

1. Now we are going to pull a docker container with all of our spark dependencies. Run the following on you EC2 instance:
```bash
sudo docker pull metisbootcamp/metis-spark-python:latest

sudo docker run -d -p 8888:8888 -v /home/ubuntu/notebooks:/home/ubuntu/notebooks \
                              metisbootcamp/metis-spark-python:latest
```
The slash allows your comment to run over multiple lines, it is **not** a typo.

The first command pulls the docker container metis has put together with a lot of Spark material. It should look similar to the command we used yesterday.

The second command makes the docker image's port 8888 available to be available to the AWS's port 8888. This is the port that Jupyter notebooks run on by default, so making this connection will allow us to interact with the notebook. It also shares the directory `/home/ubuntu/notebooks/' we just created between the EC2 instance and the Docker image.

2. Get the container id, using
```bash
sudo docker ps -a
```
The output should be something like
```
CONTAINER ID IMAGE              COMMAND                CREATED       STATUS       PORTS   
41f84d1bf747 metis-spark-python "/bin/bash /home/ubun" 2 seconds ago Up 2 seconds 0.0.0.0:8888->8888/tcp
```
In this case, we would copy 41f84d1bf747. Your id will (almost certainly) be different.

## Test the installation (all run on AWS)

We will check that the container installed properly. 

1. Run
```bash
sudo docker exec -it _container_id_ pyspark
```
where `_container_id_` is the id we copied above. For example, I would run `docker exec -it 41f84d1bf747 pyspark`

This will take me to pyspark (which lives on my Docker container, which is running in my AWS instance).

You can also try
```bash
sudo docker run -it metis-spark-python pyspark
```

2. Run the following in PySpark. Don't copy and paste, actually try running it:
```python
Python 3.6.0 |Continuum Analytics, Inc.| (default, Dec 23 2016, 12:22:00)
[GCC 4.4.7 20120313 (Red Hat 4.4.7-1)] on linux
Type "help", "copyright", "credits" or "license" for more information.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /__ / .__/\_,_/_/ /_/\_\   version 2.1.1
      /_/

Using Python version 3.6.0 (default, Dec 23 2016 12:22:00)
SparkSession available as 'spark'.
>>> docs = ["This is document one",
            "This is document two",
            "This is document three",
            "This is yet another document",
            "Make the document list stop"]
    # sc is the SparkContext (defined by default in PySpark)
>>> doc_rdd = sc.parallelize(docs)
>>> lazy_vectorize = doc_rdd.flatMap(lambda doc: doc.lower().split(" ")).map(lambda word: (word, 1)).reduceByKey(lambda a,b: a+b)
    # Note that lazy_vectorize hasn't done anything yet
>>> lazy_vectorize
PythonRDD[5] at collect at <stdin>:1
    # Now actually run it
>>> lazy_vectorize.collect()
<What does this output mean??>
>>> exit()
```

This is pretty cool: if we had millions of documents, Spark would be able to send out different documents to get `flatMap`ped and `map`ped on different machines (the results of `flatMap` and `map` only rely on what is happening in a single document), and `reduceByKey` combines documents two at a time. We have built a parallelizable CountVectorizer!

When you are done testing, you can exit your AWS instance. Don't stop it yet, however.

## Run a Jupyter notebook on AWS (run from YOUR machine)

1. Copy the Jupyter notebooks from today's lectures to your AWS instance. You have to be in the directory for today's lectures for this to work
```bash
scp -i ~/.ssh/aws_key.pem *.ipynb ubuntu@xxx.xxx.xxx.xxx:notebooks/
scp -i ~/.ssh/aws_key.pem data/*.txt ubuntu@xxx.xxx.xxx.xxx:notebooks/data/
```

2. Now we will connect our computer's port 12345 to AWS's port 8888 (which is also connected to Docker's port 8888, which is where Jupyter notebooks live). Confused yet? Type the following command on your _local machine_
```bash
ssh -i ~/.ssh/aws_key.pem -NL 12345:localhost:8888 ubuntu@xxx.xxx.xxx.xxx
```
This command will never return. Minimize the window, but **don't** close it

3. Open a browser window, and navigate to http://localhost:12345. You should be connected to Jupyter, running on your AWS instance.

Notice that if you forgot to upload a file, you can use the UPLOAD button in the top right of the screen (next to "NEW") to upload files from your local machine to your Docker instance.

### FAQ:
* **Why did we connect to port 12345? Could I use a different port?**
Yes. We chose the port the local machine used in step 2. You want to avoid ports being used by other services, so don't use anything below 1000. Don't use 8888, 8889, 8890, etc, as they might already be in use by Jupyter on your local machine.

* **What if my computer disconnects because of Network issues? Can I turn my computer off during a long calculation?**
Jupyter will still keep running in the background on AWS. You just need to reconnect your browser. If you just closed the browser window, and your SSH tunnel is still active, you can reconnect simply by going back to http://localhost:12345. If your computer turned off, or your network was disrupted, you may need restablish the SSH "tunnel" between ports 12345 on your machine, and 8888 on your Docker container. To do this, rerun
```bash
ssh -i ~/.ssh/aws_key.pem -NL 12345:localhost:8888 ubuntu@xxx.xxx.xxx.xxx
```
Then you can use your browser to load http://localhost:12345.

* **I get an error saying that the port 12345 is used, but I cannot connect** 

Kill the ssh process you started, to free it, then restart it.

* **I get a Py4JNetworkError: An error occurred while trying to connect to the Java server (127.0.0.1:12345)**

Your instance probably ran out of memory (RAM)! Bump up your T2.micro to a larger tier for a faster and more consistent computation.
