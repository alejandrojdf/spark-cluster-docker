from pyspark.sql import SparkSession
# from faker import Faker

# fk = Faker('en-GB')

# def create_person(num_records):
#     data = []
#     for _ in range(num_records):
#         data.append({'name' : fk.name(),
#                     'last_name' : fk.last_name(),
#                     'address' : fk.address().replace('\n', ' '),
#                     'phone_number' : fk.phone_number()})
#     return data

data = [{"Category": 'Category A', "ID": 1, "Value": 12.40},
        {"Category": 'Category B', "ID": 2, "Value": 30.10},
        {"Category": 'Category C', "ID": 3, "Value": 100.01}
        ]

spark = SparkSession.builder \
    .appName('cluster-test') \
    .getOrCreate()


df =  spark.createDataFrame(
    [
        (1, 'foo'), # create your data here, be consistent in the types.
        (2, 'bar'),
    ],
    ['id', 'txt'] # add your columns label here
)

# df = spark.createDataFrame(data)
print(df.schema)
df.show()
# .master('localhost') \

# spark.createDataFrame(create_person(100)).show()


