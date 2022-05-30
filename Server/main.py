from modbusServer import modbusServer

#instanciando a classe:
s = modbusServer('localhost',502)#a porta é a padrão do protocolo
s.run()