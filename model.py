import web, datetime

db_host='wvulqmhjj9tbtc1w.cbetxkdyhwsb.us-east-1.rds.amazonaws.com'
db_name='l22tx2f3v48q214'
db_user='i7h07ld9mdjw67z4'
db_pw='ms9on7mxisxizvzh'

db=web.database(
  dbn='mysql',
  host=db_host,
  db=db_name,
  user=db_user,
  pw=db_pw
	)

def get_posts():
    return db.select('alumnos', order='id_alumno ASC')

def get_post(id_alumno):
    try:
        return db.select('alumnos', where='id_alumno=$id_alumno', vars=locals())[0]
    except:
        return None

def new_post(nombre, apellidos, sexo, curp):
    db.insert('alumnos', nombre=nombre, apellidos=apellidos, sexo=sexo, curp=curp, posted_on=datetime.datetime.utcnow())

def del_post(id_alumno):
    db.delete('alumnos', where="id_alumno=$id_alumno", vars=locals())

def update_post(id_alumno, nombre, apellidos, sexo, curp):
    db.update('alumnos', where="id_alumno=$id_alumno", vars=locals(),
        nombre=nombre, apellidos=apellidos, sexo=sexo, curp=curp, posted_on=datetime.datetime.utcnow())