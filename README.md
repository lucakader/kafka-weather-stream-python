Developed a weather data processing system using Kafka streams in Python. A Kafka producer was created to stream daily weather data into a topic, while consumers were implemented to process the data. One consumer generates JSON summary statistics for use in a web dashboard, and another visualizes key weather trends. Ensured 'exactly-once' semantics for data processing, manually managed Kafka topics and partitions, and implemented atomic writes to prevent partial file updates. Statistical metrics like average temperature were tracked, and visual plots were generated from the processed data.
