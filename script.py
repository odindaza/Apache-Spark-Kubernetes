from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, lower
import sys

def main() -> None:
    print("[*] Creating the Spark session...")
    spark = SparkSession.builder \
        .appName("ProcesamientoBatch") \
        .master("spark://spark-master-service:7077") \
        .getOrCreate()
    print("[+] Session created on spark://spark-master-service:7077\n")

    print("[*] Loading the dataset...")
    dataset = spark.read.csv(sys.argv[1], header=True, inferSchema=True)
    print(f"[+] The dataset '{sys.argv[1]}' has been loaded.\n")

    print("[*] Cleaning null values from the dataset...")
    clean_dataset = dataset.dropna()
    print("[+] Null values removed.\n")

    print("[*] Transforming the dataset...")
    transformed_dataset = clean_dataset.withColumn(
        "DESCRIPCION CONDUCTA CAPTURA",
        lower(col("DESCRIPCION CONDUCTA CAPTURA"))
    )
    averages_by_gender = transformed_dataset.groupBy("GENERO") \
        .agg(avg("CODIGO DANE").alias("Promedio Codigo DANE"))
    averages_by_gender.show()
    print("[+] Dataset transformation complete.\n")

    print("[*] Saving the results...")
    averages_by_gender.write.parquet("reported.parquet")
    print("[+] Results saved in 'reported.parquet'.\n")

    spark.stop()
    print("[*] Spark session stopped.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} [DATASET]")
        print(f"\tExample: {sys.argv[0]} dataset_store.csv")
        print("Note: The dataset must be a file with the extension .csv")
    else:
        main()
