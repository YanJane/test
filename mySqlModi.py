#coding=utf-8
import MySQLdb
import re

'''
function:

remove '(一)'，when there is no '(二)' in 'content' of  mysql table

'''



#connect to mysql database
conn = MySQLdb.connect(host="localhost",user="root",passwd="ROOT",db="Nanwu",charset='utf8')
cursor = conn.cursor()
cursor.execute("SELECT * from bud_content")

special1 = '\(一\)'
special2 = '\(二\)'

for x in range(1,cursor.rowcount+1):

	cursor.execute("SELECT * from bud_content where id=%s" %x)
	temp = cursor.fetchone()[1].encode('utf-8')
	if re.match(r'.*%s.*[^%s].*' % (special1,special2),temp):
		temp=re.sub(r'%s' % special1,r'',temp)
		cursor.execute('update bud_content set content= "%s" where id=%s' %(temp,x))
		conn.commit()


conn.close()
