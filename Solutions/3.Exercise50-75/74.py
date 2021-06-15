import pandas

data1 = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2 = pandas.read_csv("sampledata_x_2.txt")
data1n2 = pandas.concat([data1, data2])
data1n2.to_csv("sampledata12.txt", index=None)