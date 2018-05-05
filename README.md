# Reference:

* Python Numpy Tutorial: http://cs231n.github.io/python-numpy-tutorial/
* 10 Minutes to Pandas: http://pandas.pydata.org/pandas-docs/stable/10min.html
* Time Series Data Virtualization with Python: https://machinelearningmastery.com/time-series-data-visualization-with-python/
* Matplotlib Animation Tutorial: https://jakevdp.github.io/blog/2012/08/18/matplotlib-animation-tutorial/


# For HDFS3 connection

Install libhdfs3(https://github.com/ContinuumIO/libhdfs3-downstream) first, then install hdfs3(https://github.com/dask/hdfs3) python package


## Download LIBHDFS3 from source code
```
# git clone https://github.com/ContinuumIO/libhdfs3-downstream.git --recursive
```

## Install googletest(Option)

To install libhdfs3, have to install googletest first
```
# cd libhdfs3-downstream/incubator-hawq/depends/thirdparty/googletest

# mkdir gbuild && cd gbuild && cmake .. && make
# cp -r googletest/include/gtest /usr/local/include
# cp googlemock/gtest/lib*.a /usr/local/lib
# cp googlemock/lib*.a /usr/local/lib
```

## Install libhdfs3
```
# cd libhdfs3-downstream/libhdfs3
# mkdir build; cd build
# ../bootstrap --help
```

Install dependencies( don't forget "+devel" ) for libhdfs3, then run installation

```
# ../bootstrap
# make
# make install
# cp ../dist/lib/libhdfs3* /usr/lib64
# cp ../dist/include/hdfs /usr/include/
```

If failed by googletest can't be found. Comment it out from CMakeLists.txt file(https://github.com/conda-forge/libhdfs3-feedstock/blob/master/recipe/CMakeLists.txt.diff)

## 