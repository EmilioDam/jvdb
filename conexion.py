import subprocess

comando = "c:\\xampp\\htdocs\\jvdb\\jvdb.exe insert miempresa clientes cliente5	 'Este es el cliente 5'"
resultado = subprocess.run(comando,shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)

if resultado.returncode == 0:
    print("ok")
else:
    print("ko")
