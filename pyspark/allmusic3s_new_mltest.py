import pandas as pd
import numpy as np
import pyspark.pandas as ps
from pyspark.sql import SparkSession
from pyspark.ml.feature import StringIndexer, MinMaxScaler,VectorAssembler
from pyspark.ml import Pipeline

from pyspark.ml.classification import LogisticRegression, RandomForestClassifier, GBTClassifier

# Local mode
spark = SparkSession.builder.appName("sqldemo").getOrCreate()

# standalone mode
#spark = SparkSession\
#        .builder\
#        .master("spark://master.example.org:7077")\
#        .config('spark.cores.max','1')\
#        .config('spark.executor.memory','1G')\
#        .appName("clusterdemo")\
#        .getOrCreate()

spark.conf.set("spark.sql.execution.arrow.pyspark.enabled", True)

sdf_3s = spark.read.csv('allmusic3s_new.csv', sep=",", header=True, inferSchema=True)
sdf_3s.createOrReplaceTempView("dfTable")
sdf_3s = sdf_3s.dropna(how='any')

sdf_cols = sdf_3s.columns
select_sdf_3s = sdf_3s.select(sdf_cols[1:])
continuous_features = [d[0] for d in select_sdf_3s.dtypes if (d[1] != 'string')]

indexers = [StringIndexer(inputCol="label", outputCol="y")]
assemblers = VectorAssembler(inputCols=[col for col in continuous_features], outputCol="features")
mmScalers = MinMaxScaler(inputCol="features", outputCol="mmfeatures")
pipeline = Pipeline(stages= [assemblers, mmScalers] + indexers)
scalerModel = pipeline.fit(select_sdf_3s)
scaledData = scalerModel.transform(select_sdf_3s)
data = scaledData.select("features","mmfeatures", "y")
trainingData, testData = data.randomSplit([0.8, 0.2])

def select_model(algo, train, test):
    model = algo.fit(train)
    predictions = model.transform(test)
    test_result = model.evaluate(test)
    print('{} Accuracy: {:5.3f}'.format(type(algo).__name__, test_result.accuracy))

# LogisticRegression
#logr = LogisticRegression(featuresCol='mmfeatures',labelCol='y')

# RandomForest
rf = RandomForestClassifier(featuresCol='mmfeatures',labelCol='y',numTrees=1000 ,maxDepth=10)

# GBTClassifier
#gbt = GBTClassifier(featuresCol='mmfeatures',labelCol='y')

select_model(rf, trainingData, testData)
