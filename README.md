# CS5065-Homework-4

This repository contains a mapper and reducer that when used with the Hadoop Streaming API will yield summary counts for each vehicle that describe the total count, per vehicle type, that the vehicle type was involved in an incident.

## Installation
1. Copy the CSV data to hdfs
   * `hadoop fs -put <path of csv file> <destination directory on hdfs>`

## Usage
1. Run the MapReduce job
```
hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar \
-file <path to mapper.py> -mapper <path to mapper.py> \
-file <path to reducer.py> -reducer <path to reducer.py> \
-input <path on hdfs to csv data> -output <path on hdfs to put the output>
```
2. Output data is located at the location on hdfs that you chose to store the output