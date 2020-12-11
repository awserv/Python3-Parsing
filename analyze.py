#!/bin/python3

import sys

fname = sys.argv[1]
f = open(fname, 'r')
s = f.read()
lines = s.split("\n")
#print(lines)


ips = set()
for line in lines :
	elems = line.split(' ')
	ip = elems[0]
#	print(ip)
	ips.add(ip)

ips = sorted(list(ips))
for ip in ips :
	print(ip)

#print(sorted(list(ips)))    # показывает сколькот файл access.log имеет  ошибочный файлов 404 200
httpCodes = [ 200, 404 ]
code200 = 0
code404 = 0
for line in lines :
	if len(line) != 0 :  # !=0  означает не равно # == сравнить на равенство
		elems = line.split(' ')
		try :  
			code = int(elems[8])    # статистика сколько клиентов получидло 200 сколько 404
			if code == 200 :
				code200 = code200 + 1
			if code == 404 :
				code404 = code404 + 1
		except : # если не выполнил TRY тогда сделать exept а в except написано pass этот ничего не делать
			pass

print('All:',  len(lines), ' 200:', code200,  ' 404:', code404)    # сколько всего строк сколько ответов 200 и сколько ответов 404



log = open('./stat.log', 'a') # a - на добавление  дописывать
codeReport = []  # создаем log file куда будем посылать отчеты

nLine = 0
for line in lines :
	nLine = nLine + 1
	if len(line) != 0 :
		elems = line.split(' ')
		try :     # достаем IP  адрес на 8 строчке с файла access.log
			code = elems[8]
			ip = elems[0]
			p = False
			for i in codeReport :
				if i.get(ip, False) != False :
					p = True
			if p == False :
				codeReport.append( { ip : {"200" : 0, "404" : 0} } )
			for i in codeReport : # просматриваем был ли файл такой то
				if i.get(ip, False) != False :
					codes = i[ip]   # 
					if code == "200" :
						codes["200"] = codes["200"] + 1
					if code == "404" :
						codes["404"] = codes["404"] + 1

		except:
			s = 'Line:' + str(nLine) + ' incorrect status code' + "\n"
			log.write(s)

for i in  codeReport :
 	print(i)




#line = lines[0]
#elems = line.split(' ')
#j = 0
#for elem in elems :
#	print(j, ' ', elem)
#	j = j + 1



