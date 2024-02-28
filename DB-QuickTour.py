# Databricks notebook source
print("Hello world")

# COMMAND ----------

# MAGIC %sql
# MAGIC select "Hello SQL!"

# COMMAND ----------

dbutils.fs.ls('/')

# COMMAND ----------

#Disply Stores in table format
files=dbutils.fs.ls('/')
display(files)
