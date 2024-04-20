import mysql.connector


def database(key):
       db = mysql.connector.connect(
           host="bx9q0wtcxb0065zsduco-mysql.services.clever-cloud.com",
           user="ucxrx4v9si7xd8j7",
           password="WqsTTpzcrp7jDik9ORTI",
           database="bx9q0wtcxb0065zsduco"
       )
       
       if db.is_connected:
           print("connected")
       else:
           print("connection fail")
           
       cursor = db.cursor()
       
       cursor.execute("SELECT value FROM moko WHERE user = %s", (str(key),))
       
       result = cursor.fetchall() 
       
       db.close()
       
       if len(result) != 0:
           return result[0][0]
       else:
           return []
