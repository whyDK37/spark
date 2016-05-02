
from pyspark import SparkConf, SparkContext
conf = SparkConf().setMaster("local").setAppName("My App")
sc = SparkContext(conf = conf)
lines = sc.textFile("first.py")
pythonLines = lines.filter(lambda line: "Python" in line)
print "hello python"
print pythonLines.first()
print pythonLines.first()
print "hello spark!"