from pyspark.sql import SparkSession
from faker import Faker
fk = Faker('en-GB')
import os

# Needed to sync spark versions when submitting spark application from outside the docker cluster
os.environ['PYSPARK_PYTHON'] = '/usr/bin/python3.7'
os.environ['PYSPARK_DRIVER_PYTHON'] = '/usr/bin/python3.7'


def create_person(num_records):
    data = []
    for _ in range(num_records):
        data.append({'name' : fk.name(),
                    'last_name' : fk.last_name(),
                    'address' : fk.address().replace('\n', ' '),
                    'phone_number' : fk.phone_number()})
    return data

data = [{"Category": 'Category A', "ID": 1, "Value": 12.40},
        {"Category": 'Category B', "ID": 2, "Value": 30.10},
        {"Category": 'Category C', "ID": 3, "Value": 100.01}
        ]

spark = SparkSession.builder \
    .appName('cluster-test') \
    .getOrCreate()

df = spark.createDataFrame(create_person(10))

df.show(500)

# df.coalesce(1).write.format('com.databricks.spark.csv').option('header', 'true').save('/Users/alejandroferrin/UdemyProjects/spark-cluster-docker/output')
# df.write.format('com.databricks.spark.csv').option('header', 'true').mode('overwrite').save('/Users/alejandroferrin/UdemyProjects/spark-cluster-docker/output')
# df.coalesce(1).write.format('json').mode("append").option("header","true").save('spark-masteroutput')