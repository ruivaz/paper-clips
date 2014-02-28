import MySQLdb


db = MySQLdb.connect(host="localhost", user="root", db="test")

cur = db.cursor()

cur.execute("select name, gpa from (select Avg(enrollment.coursename) as gpa, enrollment.studentid from enrollment group by enrollment.studentid) honors join student on honors.studentid = student.id order by gpa DESC")

for row in cur.fetchall():
  print row
