from database.db import get_connection

#Seguridad
from utils.Security import Security
#Reciclado Maquina
from .entities.RecicladoMaquina import RecicladoMaquina

class RecicladoMaquinaModel():
    
    @classmethod
    def get_RecicladoMaquina(self,OidMaquina):
        # oid = Security.validar_uuid(OidMaquina)
        # if oid == False:
        #     return {
        #         'status': False,
        #         'mensaje': "Valor Invalido",
        #     }
        # else:
            try:
                connection = get_connection()

                reciclados = []
                monto = 0
                with connection.cursor() as cursor:
                    sql="""SELECT rm."Oid",rm."Maquina",to_char(rm."Fecha",'dd-MM-yyyy'),rm."Cantidad",rm."Monto"
                                    FROM "RecicladoMaquina" rm
                                    WHERE rm."Maquina" = %s"""
                    cursor.execute(sql, (OidMaquina,))
                    resultset = cursor.fetchall()
                    for row in resultset:
                        recicladoM = RecicladoMaquina(row[0],row[1],row[2],row[3],row[4])
                        monto+=row[4]
                        reciclados.append(recicladoM.to_JSON())
                connection.close()
                return {
                    'status': True,
                    'mensaje': "Exitoso",
                    'recicladoMaquina': reciclados,
                    'Total': len(reciclados),
                    'Suma': monto
                }
            except Exception as ex:
                raise Exception(ex)
    
    @classmethod
    def add_RecicladoMaquina(self,reciclado):
        # oid = Security.validar_uuid(reciclado.Maquina)
        # if oid == False:
        #     return {
        #         'status': False,
        #         'mensaje': "Valor Invalido",
        #     }
        # else:
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
                        sql="""INSERT INTO "RecicladoMaquina" ("Oid", "Maquina", "Fecha", "Cantidad", "Monto") 
                            VALUES ((SELECT(uuid_in(overlay(overlay(md5(random()::text || ':' || clock_timestamp()::text) placing '4' from 13) placing to_hex(floor(random()*(11-8+1) + 8)::int)::text from 17)::cstring))),
                            %s, (SELECT NOW()), 1,0.10) RETURNING "Oid" """
                        cursor.execute(sql, (reciclado.Maquina,))
                        connection.commit()

                        affected_rows = cursor.rowcount

                        connection.close()
                        
                        if affected_rows == 1:
                            return {
                                'status': True,
                                'mensaje': "Guardado Exitosamente",
                            }
                        else:
                            return {
                                'status': False,
                                'mensaje': "Error al Guardar Reciclado"
                            }
            except Exception as ex:
                return {
                    'status': False,
                    'mensaje': Exception(ex)
                }

    @classmethod
    def delete_RecicladoMaquina(self,reciclado):
        # oid = Security.validar_uuid(reciclado.Maquina)
        # if oid == False:
        #     return {
        #         'status': False,
        #         'mensaje': "Valor Invalido",
        #     }
        # else:
            try:
                #Elimina los registros de RecicladoMaquina
                connection = get_connection()
                with connection.cursor() as cursor:
                    sql="""DELETE FROM "RecicladoMaquina" WHERE "Maquina"=%s """
                    cursor.execute(sql, (reciclado.Maquina,))
                    connection.commit()
                connection.close()
                return {
                    'status': True,
                    'mensaje': "Inicio de Maquina"
                }
            except Exception as ex:
                return {
                    'status': False,
                    'mensaje': Exception(ex)
                }
