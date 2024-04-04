from database.db import get_connection

#Seguridad
from utils.Security import Security
#Persona
from .entities.Persona import Persona

class PersonaModel():

    @classmethod
    def datos_generales(self,header):
        usuario = Security.verify_token(header)
        if usuario==None:
            return {
                'status': False,
                'mensaje': 'Tiempo finalizado'
            }
        else:
            try:
                connection = get_connection()
                with connection.cursor() as cursor:
                    sql="""SELECT p."Oid", p."Nombre", p."PrimerApellido", p."SegundoApellido", p."Correo", p."Telefono", p."Ciudad", to_char(p."FechaRegistro",'dd-MM-yyyy'), p."Observaciones", 
                            coalesce(sum(r."Monto"),0)  as "TotalReciclado", coalesce(sum(r2."Monto"),0) as "TotalRetirado",
                            coalesce(sum(r."Monto")-sum(r2."Monto"),0) as "TotalDisponible"
                        FROM "Persona" p
                        left join "Reciclado" r on r."Persona"  = p."Oid" 
                        left join "Retiro" r2 on r2."Persona"  = p."Oid" 
                        WHERE p."Oid" = %s
                        group by p."Oid" """
                    cursor.execute(sql, (usuario['Oid'],))
                    persona = cursor.fetchone()
                connection.close()
                
                if persona == None:
                    return {
                        'status': False,
                        'mensaje': "Datos no encontrados",
                    }
                else:
                    personaEnt = Persona(persona[0],persona[1],persona[2],persona[3],persona[4],persona[5],persona[6],persona[7],persona[8],persona[9],persona[10],persona[11])
                    return {
                        'status': True,
                        'mensaje': "Exitoso",
                        'persona': personaEnt.to_JSON()
                    }
            except Exception as ex:
                raise Exception(ex)
            