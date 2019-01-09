### Python bindings for Postgres

How can you access data in Postgres from Python? Using the `psycopg2` module, you can execute any query and get the results in python to do whatever you want to them (put it in `pandas`, throw it into `sklearn` algorithms, etc.)

Here again it will be easier to `apt-get install` than `pip install`:

```bash
sudo apt-get install python-psycopg2
```

Then, in Python:

```python
import psycopg2

db = psycopg2.connect(database='endor')
cursor = db.cursor()

cursor.execute("select * from ewoks;")

for row in cursor.fetchall():
    print row
```
