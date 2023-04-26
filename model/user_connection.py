import psycopg


class UserConnection():
    conn = None

    def __init__(self):
        try:
            self.conn = psycopg.connect(dbname="fastapi_test", user="postgres", password="postgres", host="localhost",
                                        port="5432")
        except psycopg.OperationalError as err:
            print(err)
            self.conn.close()



    # Esta es la primera sentencia de nuestro CRUD , la de escribir datos
    def write(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                   INSERT INTO "user"(name, phone) VALUES(%(name)s, %(phone)s)
               """, data)
        self.conn.commit()



    # Método que nos permite leer todos los datos
    def read_all(self):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                SELECT * FROM "user"
            """)
            return data.fetchall()


    # Método que nos permite leer un solo dato
    def read_one(self, id):
        with self.conn.cursor() as cur:
            data = cur.execute("""
                   SELECT * FROM "user" WHERE id=%s
               """, (id,))
            return data.fetchone()



    # Esta es la función para Borrar
    def delete(self, id):
        with self.conn.cursor() as cur:
            cur.execute("""
                   DELETE FROM "user" WHERE  id= %s
               """, (id,))
        self.conn.commit()


    # Esta es la función para Actualizar, cuando se pasa el data va sin parentesis
    def update(self, data):
        with self.conn.cursor() as cur:
            cur.execute("""
                UPDATE  "user"  SET name=%(name)s, phone=%(phone)s WHERE id =%(id)s
            """, data)
        self.conn.commit()

    # Esto es un destructor
    # def __def__(self):
    # self.conn.close()
