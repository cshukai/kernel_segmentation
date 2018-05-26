#continue from preprocessing/paralle.hdfs.py

from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator


# Apache spark 2.x machine learning cookbook [electronic resource] : over 100 recipes to simplify machine learning model implementations with Spark / Siamak Amirghodsi, Meenakshi Rajendran, Broderick Hall, Shuen Mei.
# the example from this book , k mean works for dataframe , however, mmlspark's dataframe can be unicode hell for spark's kmean
# offical python example:https://spark.apache.org/docs/latest/ml-clustering.html#k-means
# k means clustering : try k =3
def findBondary(row):
    deeperRow=row.transformed
    arr=toNDArray(deeperRow)