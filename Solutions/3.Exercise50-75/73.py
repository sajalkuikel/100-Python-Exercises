import pandas

# data = pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
# data_2 = data * 2
# data_2.to_csv("sampledata_x_2.txt", index=None)

data= pandas.read_csv("http://www.pythonhow.com/data/sampledata.txt")
data2= data * 2
data2.to_csv("newsample.txt", index=None)