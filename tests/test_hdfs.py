from unittest import TestCase

from hdfs3 import HDFileSystem
import pandas

class test_hdfs(TestCase):
    def test_hdfs_csv(self):
        '''
        HDFS3 Configuration:
          https://hdfs3.readthedocs.io/en/latest/hdfs.html
        '''
        dfs =  HDFileSystem(host="localhost", port=8020, user="hadoop")
        dfs.mkdir("/temp")
        dfs.put("tests/data/data.csv", "/temp/data.csv")

        with dfs.open("/temp/data.csv") as f:
            df = pandas.read_csv(f, nrows=10)
            print("Data shape from HDFS: " + str(df.shape))
        
        dfs.rm("/temp/data.csv")

    def test_webhdfs_csv(self):
        from pywebhdfs.webhdfs import PyWebHdfsClient
        dfs = PyWebHdfsClient(host='localhost',port='9870', user_name='hadoop')
        dfs.make_dir("/temp")

        with open("tests/data/data.csv") as input_file:
            dfs.create_file("/temp/data.csv", file_data=input_file, overwrite=True)

        dfs.delete_file_dir("/temp", recursive=True)