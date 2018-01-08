#encoding=utf-8
import csv
import pygal
from matplotlib import pyplot as plt

filename = 'movie_details.csv'
with open(filename) as f:
	reader = csv.reader(f)
	head_row = next(reader)

	first_lie = []
	second_lie = []
	third_lie = []
	fourth_lie = []
	fifth_lie = []
	sixth_lie = []
	seventh_lie =[]
	for row in reader:
		first_lie.append(row[0]) #电影名称
		
		if (row[3])[-1] == '亿': #实时票房
			s = (row[3])[0:-1]
			s1 = 10000 * float(s) 
			second_lie.append(s1)
		if (row[3])[-1] == '万':
			s2 = float((row[3])[0:-1])
			second_lie.append(s2)

		if (row[2])[-1] == '亿': #总票房
			s = (row[2])[0:-1]
			s1 = 10000 * float(s) #将字符串由字符转为float再乘以10000
			third_lie.append(s1)
		if (row[2])[-1] == '万':
			s2 = float((row[2])[0:-1])
			third_lie.append(s2)
		four = float((row[4])[0:-1])/100  #票房占比
		fourth_lie.append(four)
		four = float((row[5])[0:-1])/100  #排片占比
		fifth_lie.append(four)
		four = float((row[6])[0:-1])/100  #上座率
		sixth_lie.append(four)
		four = float((row[7])[0:-1])/100  #占座比率
		seventh_lie.append(four)
	print(fourth_lie)
	print(second_lie)
	
	hist = pygal.Bar()
	hist.title = "Result of the movies "
	hist.x_title = "电影名称"
	hist.y_title = "电影票房数 (单位：万)"
	hist.x_labels = first_lie
	hist.add("总票房",third_lie)
	hist.render_to_file('总票房.svg')

	pie_chart = pygal.Pie()
	pie_chart.title = '票房所占比例'
	i = 0
	for x in first_lie:
		pie_chart.add(first_lie[i], fourth_lie[i])
		i = i+1
	pie_chart.render_to_file('票房所占比例.svg')

	j = 0
	radar_chart = pygal.Radar()
	radar_chart.title = '电影总数据雷达图'
	radar_chart.x_labels = head_row[2:7]
	radar_chart.x_labels[0] = radar_chart.x_labels[0]+"(单位：十亿)"
	radar_chart.x_labels[1] = radar_chart.x_labels[0]+"(单位：亿)"
	while j < 20:
		radar_chart.add(first_lie[j], [third_lie[j]/100000, second_lie[j]/10000, fourth_lie[j],fifth_lie[j],sixth_lie[j],seventh_lie[j]])
		j = j+1
	print(j)
	radar_chart.render_to_file('总数据雷达图.svg')
