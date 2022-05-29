#criação do servidor: fornece dados por esse protocolo
#passo 1: criar ambinte virtual para baixar as bibliotecas necessárias
from pyModbusTCP.server import DataBank, ModbusServer
from time import sleep

import random


class modbusServer():
    """
    Modbus Class Server
    """

    def __init__(self, host_ip, port):#construtor: receiving ip server and port
        
        self._server = ModbusServer(host = host_ip, port = port,no_block=True)
        #objeto da classe modbusServer que encapsula todos os procedimentos de recepção de dados
        #e desencapsula dados além de atendimento/resposta aos clientes: no_block= true cria
        #thread pra atender cliente
        self._db = DataBank
        #objeto que, quando criado, possuirá as tabelas do servidor

    def run(self):
        """
        Execução do servidor Modbus
        """
        try: 
            self._server.start()#inicializa o sistema
            print("Modbus server execution")
            while True:
                #alterar valor de um registrador para ficar verificando no cliente
                self._db.set_words(1000,[random.randrange(int(0.95*400),int(1.05*400))])#determinar o valor de uma palavra num derterminado registro no db
                #há basicamente 2 tabelas no databank do modbusServer: word e bits
                #e não 4 tabelas como na implementação classica do modbus  
                print('-----------------')
                print("MODBUS table")
                print(f'Holding Register \r\n R1000: {self._db.get_words(1000)} R2000: {self._db.get_words(2000)}' )
                print(f'Coll \r\n R1000: {self._db.get_bits(1000)}')
                sleep(1)
        except Exception as e:
            print("Error: ", e.args)
