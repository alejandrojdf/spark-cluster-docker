# spark-cluster-docker

spark-submit --master spark://spark-master:7077 test/cluster-test.py

spark-submit --master spark://spark-master:7077 --executor-memory 900M --total-executor-cores 1 --driver-memory 500M --num-executors 1  test/cluster-test.py
