#continue from preprocessing/paralle.hdfs.py

from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator
from pyspark.ml.linalg import Vectors

data = [(Vectors.dense([0, 0]),), (Vectors.dense([1.0, 1.0]),),(Vectors.dense([9.0, 8.0]),), (Vectors.dense([8.0, 9.0]),)]
# Apache spark 2.x machine learning cookbook [electronic resource] : over 100 recipes to simplify machine learning model implementations with Spark / Siamak Amirghodsi, Meenakshi Rajendran, Broderick Hall, Shuen Mei.
# the example from this book , k mean works for dataframe , however, mmlspark's dataframe can be unicode hell for spark's kmean
# offical python example:https://spark.apache.org/docs/latest/ml-clustering.html#k-means
# k means clustering : try k =3
df = map(lambda x: Vectors.dense(x), )
df2 = spark.createDataFrame(df,["features"])
#https://stackoverflow.com/questions/46901938/big-numpy-array-to-spark-dataframe
# TypeError: not supported type: <type 'numpy.ndarray'>
# >>> type(df)



def ColumnCorrFiltering(row):
    deeperRow=row.image
    arr=toNDArray(deeperRow)
    r_rdd=spark.sparkContext.parallelize(arr[:,:,0])
    g_rdd=spark.sparkContext.parallelize(arr[:,:,1])
    b_rdd=spark.sparkContext.parallelize(arr[:,:,2])


def findBondary(row):
    deeperRow=row.image
    arr=toNDArray(deeperRow)       