from database.db import get_connection

#Seguridad
from utils.Security import Security
#entidades
from .entities.Reciclado import Reciclado
#Modelo
from models.RecicladoMaquinaModel import RecicladoMaquinaModel

class RecicladoModel():
    
    @classmethod
    def get_Reciclados_Persona(self,header):
        usuario = Security.verify_token(header)
        if usuario == None:
            return {
                'status': False,
                'mensaje': "Tiempo finalizado",
            }
        else:
            try:
                connection = get_connection()

                reciclados = []
                monto = 0
                with connection.cursor() as cursor:
                    sql="""SELECT r."Oid",r."Persona",r."Maquina",to_char(r."Fecha",'dd-MM-yyyy'),r."Cantidad",r."Monto"
                                    FROM "Reciclado" r
                                    WHERE r."Persona" = %s
                                    ORDER BY r."Fecha" DESC"""
                    cursor.execute(sql, (usuario['Oid'],))
                    resultset = cursor.fetchall()
                    for row in resultset:
                        reciclado = Reciclado(row[0],row[1],row[2],row[3],row[4],row[5])
                        monto+=row[4]
                        reciclados.append(reciclado.to_JSON())
                connection.close()
                return {
                    'status': True,
                    'mensaje': "Exitoso",
                    'reciclado': reciclados,
                    'Total': len(reciclados),
                    'Suma': monto
                }
            except Exception as ex:
                raise Exception(ex)
    
    @classmethod
    def add_Reciclado_SinP(self,reciclado):
        try:
            connection = get_connection()
            with connection.cursor() as cursor:
                sql_buscar="""SELECT "Oid" FROM "Maquina" 
                                WHERE "Oid"=%s"""
                cursor.execute(sql_buscar, (reciclado.Maquina,))
                maquina=cursor.fetchone()
            connection.close()
            if maquina == None:
                return {
                    'status': False,
                    'mensaje': "Maquina no registrada"
                }
            else:
                connection = get_connection()
                with connection.cursor() as cursor:
                    sql="""SELECT rm."Maquina",(select NOW()),COUNT(*),SUM(rm."Monto")
                                FROM "RecicladoMaquina" rm
                                WHERE rm."Maquina" = %s
                                group by rm."Maquina" """
                    cursor.execute(sql, (reciclado.Maquina,))
                    row = cursor.fetchone()
                connection.close()
                if row:
                    connection = get_connection()
                    with connection.cursor() as cursor:
                        sql="""INSERT INTO "Reciclado" ("Oid", "Maquina", "Fecha", "Cantidad", "Monto") 
                            SELECT 
                                (SELECT(uuid_in(overlay(overlay(md5(random()::text || ':' || clock_timestamp()::text) placing '4' from 13) placing to_hex(floor(random()*(11-8+1) + 8)::int)::text from 17)::cstring)))
                                ,rm."Maquina",(select NOW()),COUNT(*),SUM(rm."Monto")
                            FROM "RecicladoMaquina" rm
                            WHERE rm."Maquina" = %s
                            GROUP BY rm."Maquina" RETURNING "Oid" """
                        cursor.execute(sql, (reciclado.Maquina,))
                        connection.commit()
                        inserted_row = cursor.fetchone()
                    OidReciclado = inserted_row[0]  
                    connection.close()

                    #Elimina los registros de RecicladoMaquina
                    connection = get_connection()
                    with connection.cursor() as cursor:
                        sql="""DELETE FROM "RecicladoMaquina" WHERE "Maquina"=%s """
                        cursor.execute(sql, (reciclado.Maquina,))
                        connection.commit()
                    connection.close()

                    return {
                        'status': True,
                        'mensaje': "Guardado Exitosamente",
                        'reciclado': OidReciclado,
                    }
                else:
                    return {
                        'status': False,
                        'mensaje': "No hay Reciclado a guardar"
                    }
        except Exception as ex:
            return {
                'status': False,
                'mensaje': Exception(ex)
            }

    @classmethod
    def update_Reciclado_AsigP(self,header,Oidreciclado):
        usuario = Security.verify_token(header)
        if usuario == None:
            return {
                'status': False,
                'mensaje': "Tiempo finalizado",
            }
        else:
            try:
                connection = get_connection()
                with connection.cursor() as cursor:
                    sql_buscar="""SELECT "Oid" FROM "Reciclado" 
                                    WHERE "Persona" IS NULL
                                    AND "Oid"=%s"""
                    cursor.execute(sql_buscar, (Oidreciclado,))
                    row = cursor.fetchone()
                connection.close()
                if row:
                    connection = get_connection()
                    with connection.cursor() as cursor:
                        sql="""UPDATE "Reciclado" 
                                SET "Persona" = %s 
                                WHERE "Oid"=%s"""
                        cursor.execute(sql, (usuario['Oid'],Oidreciclado,))
                        connection.commit()
                    connection.close()
                    
                    return {
                        'status': True,
                        'mensaje': "Asignación de Reciclado Exitoso"
                    }
                else:
                    return {
                        'status': False,
                        'mensaje': "Reciclado ya registrado"
                    }

            except Exception as ex:
                return {
                    'status': False,
                    'mensaje': Exception(ex)
                }
