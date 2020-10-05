from airflow.contrib.sensors.gcs_sensor import GoogleCloudStoragePrefixSensor
from airflow import DAG
from datetime import datetime, timedelta
from airflow.contrib.operators.dataproc_operator import DataprocClusterCreateOperator,DataprocClusterDeleteOperator, DataProcSparkOperator
from airflow.contrib.operators.gcs_to_bq import GoogleCloudStorageToBigQueryOperator
from airflow.models import Variable

jar_location = Variable.get("jar_location")
build_id = Variable.get("BUILD_ID")

yesterday = datetime.combine(datetime.today() - timedelta(1),
                             datetime.min.time())


default_args = {
    'owner': 'Shashikant',
    'depends_on_past': False,
    'start_date' :yesterday,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 0,
    'retry_delay': timedelta(minutes=5),

}

dag = DAG(
    'example_spark_bq_airflow',catchup=False, default_args=default_args)

# DATAPROC_SPARK_PROP= {
# "spark.jars.packages":"org.apache.lucene:lucene-core:7.5.0,org.apache.lucene:lucene-queries:7.5.0,org.apache.lucene:lucene-spatial:7.5.0,org.apache.lucene:lucene-spatial:7.5.0,org.apache.lucene:lucene-spatial-extras:7.5.0,org.apache.logging.log4j:log4j-core:2.9.0,org.apache.logging.log4j:log4j-api:2.9.0,org.apache.logging.log4j:log4j-slf4j-impl:2.9.0,org.noggit:noggit:0.8,org.locationtech.jts:jts-core:1.15.0,org.locationtech.spatial4j:spatial4j:0.7,org.postgresql:postgresql:42.2.5,com.aerospike:aerospike-client:4.3.0,com.maxmind.geoip2:geoip2:2.4.0,com.google.cloud:google-cloud-storage:1.87.0",
# 'spark.executor.memoryOverhead':'2g',
# 'spark.executor.cores':'3',
# "spark.executor.memory":'8g',
# 'spark.master':'yarn',
# 'spark.driver.userClassPathFirst':'true',
# 'spark.executor.userClassPathFirst':'true',
# 'spark.yarn.maxAppAttempts':'1'
# } # Dict mentioning Spark job's properties

DATAPROC_SPARK_JARS = [jar_location]


# date_tuple = dynamic_date(3) # Suppose we are processing 3 days ago's data - mimics a lag in arrival and processing of data

run_spark_job = DataProcSparkOperator(
   dag=dag,
   arguments=["1000000"],
   region="us-west1",
   task_id ='example-job-build_id',
   dataproc_spark_jars=DATAPROC_SPARK_JARS,
#    dataproc_spark_properties=DATAPROC_SPARK_PROP,
   cluster_name='cluster-f4a8',
   main_class = 'org.apache.spark.examples.SparkPi',
)


run_spark_job
