# Databricks notebook source
# !!! Before performing any data analysis, make sure to run the pipeline to materialize the sample datasets. The tables referenced in this notebook depend on that step.

display(spark.sql("SELECT * FROM workspace.myschema.orders"))
