# Streaming map-reduce with Python


#### History and Background
> Map-reduce is a famous programming model that extends simple analytics to massive data sets, spread across HDFS - the Hadoop Distributed Filesystem.  
It is an important development of "Big Data," which has generated much excitement everywhere.  This week we will be setting up and getting started
with some big-data systems and applications, but we start here with a much smaller map-reduce problem, designed to run locally on our machines.
From an analytic viewpoint, Map-reduce is simple. Files are mapped, line by line, into key value pairs.  A "shuffle and sort" algorithm
pulls together these keys and sorts them, then sends them to a reducer program, which counts the number of occurrences of each class.  The end
results are simply counts, similar to what we would've gotten with value_counts in Pandas.  The difference is that this code might
be sent to multiple machines, each housing their own partitions of the data.  The "shuffle and sort" work happens on a master computer (name node)
which sends map and reduce tasks to worker nodes.  As a result, we are able to operate on massive datasets, much
larger than the datasets that fit on a single machine.  Much of the motivation for developing MapReduce was to build a web crawler,
capable of indexing now billions of web pages with many inter-linkages.

## Working with Tweets!

**Problem description**: Use the map-reduce programming model to count the number of tweets from each user. Your final program will be executed by running the following bash command

```bash
cat input.txt | python tweets_map.py | sort | python tweets_reduce.py
```

**Input**: input.txt contains stringified rows in dictionary data structures.
These are tweets, stored in dict form. Each tweet dict occupies a new line.

**Output**: Finally we will use a reduce function to count the sorted output by screen name to give us a final output. Example:

```
EXINMUSICA 3
IBMBigDataUK 2
JennZimm72 4
NuriaMariaT 3
...
```

**Things to consider**:

You will write two python scripts where `tweets_map.py` contains the mapping function, and `tweets_reduce.py` contains the reduce code.

A **map** function takes in *n* inputs, transforms each input individually (without reference to the others), and then produces *n* outputs.

The outputs of the map function are sorted and then piped to a *reduce* function which produces ≤*n* outputs.

The challenge of this problem is dividing the computation between map and reduce functions.

Recall that the pipes between commands indicate that the output from one function/program/command is passed to the next function/program/command.   
Cat reads the input file in and passes it to tweets_map.py, which in turn passes its output to the Unix sort function, and so on.  Your challenge is to create tweets_map.py and tweets_reduce.py.


Hints for the Mapper code:
```
1. The mapping function will have to find each user_name.  Hint: it's nested.  You might use pretty-print to figure out the data structure.  
Try using sys.stdin.readline() to read just one line and deduce its structure.
2. Look up ast.literal_eval. literal_eval(line) will turn the stringified dictionary into an actual dict data structure, from which you can use dictionary logic.
3. Use sys.stdin to read the Twitter data in streaming fashion, line-by-line.  It creates an iterator on lines.
4. We want fail-safe code.  (More on distributed fault tolerance later.)  Make sure your code doesn't bomb if it doesn't find a user_name in the line.
5. You can simply use the print function to generate output to send to the sort step.
```

Hints for the reducer code:
```
1. This code simply moves down the sorted output lines from 'sort', adding 1 to the count every time it sees a tweet from the same user.
2. When it sees a new user in the sorted output, it outputs the count from the previous user:  print(current_handle, counter) and switches current_handle to the new user and resets the counter.
3. Sometimes data contains unwanted spaces.  Use strip() to make sure they're gone.
4. We should end with just one count per user, with the count printed next to the user name and sent to the output file, one user per line.
```

You can always take steps off of the pipe. So if you aren't sure if your
mapper is working, just cut off the sort and reducer parts and see what comes
out. Is that what you want?

## Question

What's the benefit of writing code like this? Wouldn't it be easier just to write one function tweet_count_by_user.py that counts each users tweets at once?

Consider, this data file contains 25 observations in the same place. What would change if it was 25,000,000 observations distributed across a dozen systems using HDFS?

## Working with Census Data

Now let's change gears a little bit. We've seen how we can work with something
that's already well organized into JSON format for us. Let's work with data
that's a bit more "raw". In the `data` folder you'll find the data from the US
census. Your challenge is to do a few things with this using the Map Reduce
paradigm. You may want to use more than one pipeline to do so, that's up to
you.

1. Compute the average age in the data
2. Compute the value counts for income.
3. Compute the value counts for education level, but only for females.

The columns are:

```
['age','workclass','fnlwght','education','education_num','marital_status','occupation',
'priv_house_serv','race','gender','capital_gain','capital_loss','hours_per_week',
'native_country','income']
```

Take your time to try to understand how to design your mappers and reducers.
**Undertanding MapReduce is a common interview question and also a great
exercise in thinking through how challenging big data can be.**
