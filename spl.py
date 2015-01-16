# encoding: utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

@outputSchema("line:chararray")
def splitJson(line):
	final = []
	#f = open("a.json", 'r')
	#for line in f.readlines():
	#temp = line.split("\n")
	#print "---------------",
	#print line
	#if line == "\n": break
	if line is None: return final
	#t_item = temp[0].split("[")
	t_item = line.split("[")
	if t_item[0] != ']' and t_item[1] != '':
		t2_item = t_item[2].split("]")
		if t2_item[0] != '':
			item = t2_item[0].split(", ")
			for i in item:
				final.append(i.strip("\""))
	#f.close()
	return final
