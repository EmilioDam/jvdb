import subprocess


class jvdb:
    def _init_(self,basededatos):
        self.basededatos = basededatos
    def insert(self,coleccion,documento,contenido):
        self.operacion = "insert"
        self.coleccion = coleccion
        self.documento = documento
        self.contenido = contenido
            comando = '"c:\\xampp\\htdocs\\jvdb\\jvdb.exe" '+operacion+' '+basededatos+' '+coleccion+' '+documento+' "'+contenido+'"'
            resultado = subprocess.run(comando,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)
            if resultado.returncode == 0:
                return("ok")
            else:
                return("ko")
