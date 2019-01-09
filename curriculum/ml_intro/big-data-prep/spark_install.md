# Installing Spark locally

## OSX

### Things you already have installed (?)

1. Homebrew: 
   If not installed, run `/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"` in terminal
2. XCode:
   If not installed, run `xcode-select --install`

You probably have these installed already from things you have already installed in this course. These are not Spark specific.

### Things to install

1. Use homebrew to install `java` (spark relies on the java JVM to run). Run these commands in the terminal.
```bash
brew cask install homebrew/cask-versions/java8
```

Earlier versions of OSX ( <= 10.9) may also have to install `brew cask install java`. 

2. Now install `scala` and `apache-spark` using Homebrew (not there is no `cask` this time)
```
brew install scala apache-spark
```

## Ubuntu

1. First we need to get a Java install that's up to date
```bash
sudo apt-get install default-jdk
```

2. Next, we need to get Scala, the language that Spark is built in
```
sudo apt-get install scala
```

3. Now we're ready to download Spark. Go here: [Spark DL](https://www.apache.org/dyn/closer.lua/spark/spark-2.3.1/spark-2.3.1-bin-hadoop2.7.tgz). Once it's downloaded,
you can uncompress it with
```
tar -xzvf spark-2.3.1-bin-hadoop2.7.tgz
```
4. Now move to the bin folder so that the other commands below will work. 
```
cd spark-2.3.1-bin-hadoop2.7/bin
```

## Testing Install

Test if this worked by loading a spark shell in the terminal:
```bash
spark-shell
```

>If that errors out, you may on Ubuntu you may need to do:
>
>```bash
>./spark-shell
>```

After a bunch of warning messages, you should see
```
2018-05-31 13:33:19 WARN  NativeCodeLoader:62 - Unable to load native-hadoop library for your platform... using builtin-java classes where applicable
Setting default log level to "WARN".
To adjust logging level use sc.setLogLevel(newLevel). For SparkR, use setLogLevel(newLevel).
Spark context Web UI available at http://172.16.0.216:4040
Spark context available as 'sc' (master = local[*], app id = local-1527791607666).
Spark session available as 'spark'.
Welcome to
      ____              __
     / __/__  ___ _____/ /__
    _\ \/ _ \/ _ `/ __/  '_/
   /___/ .__/\_,_/_/ /_/\_\   version 2.0.1
      /_/
Using Scala version 2.11.8 (Java HotSpot(TM) 64-Bit Server VM, Java 1.8.0_102)
Type in expressions to have them evaluated.
Type :help for more information.
scala>
```

If you see something similar to this, congratulations! You have Spark installed. In the terminal, you will also see the line
```
Spark context Web UI available at http://172.16.0.216:4040
```
If you type in the URL into your browser (in my case http://172.16.0.216:4040, but yours will be different) you will get a Spark status screen that reports on the status of the different jobs Spark is running.

Quit the `spark-shell` by typing `:quit` at the prompt:
```scala
scala> :quit
```

## Hooking Spark up with Python

1. Install pyspark:

```bash
conda install pyspark
```

You have now installed Spark and PySpark on your computer!

2. Install the Python package `findspark` to help Jupyter Notebooks ..... find Spark

```bash
conda install -c conda-forge findspark
```

3a. (ONLY ON MACs) PySpark will load, but it will have problem actually connecting to the Java Virtual Machine. You need to set the environment variable JAVA_HOME. Add the following line to `~/.bash_profile`:
```bash
export JAVA_HOME=`/usr/libexec/java_home -v 1.8`
```
Either open a new terminal, or run the command
```bash
source ~/.bashrc
```

3b. (ONLY ON SOME UBUNTU) If you're getting errors when trying to us pyspark, check you version of Java with `java -version`. If it's not java-8-*stuff-here*, then you'll need to convert to Java 8.

```
sudo add-apt-repository ppa:webupd8team/java
sudo apt update
sudo apt install oracle-java8-installer
```

Then open your `~/.bashrc` and add the following line

```
export JAVA_HOME=/usr/lib/jvm/java-8-oracle/jre
```

then run `source ~/.bashrc` to make that active. Now your pyspark should find the right version of Java. 
 
4. Test that everything worked

In the terminal, run
```bash
pyspark
```

You should see the 

### Using Spark

1. From the terminal, you can run `pyspark` to load python with spark already loaded with a spark context preloaded:
```bash
pyspark  
```

**OR**

2. If you load `python` from the terminal, you can import pyspark as a package and create a context manually:
```python
$ python
Python 3.6.5 |Anaconda custom (64-bit)| (default, Apr 26 2018, 08:42:37) 
[GCC 4.2.1 Compatible Clang 4.0.1 (tags/RELEASE_401/final)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
> import pyspark
> spark = pyspark.sql.SparkSession.builder.getOrCreate() # your context!
```


Either way, you can then run:

```python
> a = spark.createDataFrame([[1,2,3],[4,5,6]])
> a.show()
```

You should see something like

```
+---+---+---+
| _1| _2| _3|
+---+---+---+
|  1|  2|  3|
|  4|  5|  6|
+---+---+---+
```

