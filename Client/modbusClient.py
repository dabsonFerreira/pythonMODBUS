from time import sleep
from pyModbusTCP.client import ModbusClient

class MODBUSClient():
    """
    Modbus Client class 
    """
    def __init__(self, server_ip, port, scan_time=1):
        #cria uma rotina que permite usuario ler x vezes um reg do servidor 
        #e o scan_time define o intervalo de leitura
        """
        Constructor
        """
        self._client = ModbusClient(host = server_ip, port = port)
        self._scan_time = scan_time
    
    def atendimento(self):
        #atendimento do usuário
        self._client.open()
        try:
            atendimento = True
            while atendimento:
                sel = input(f"Deseja realizar (1)-leitura (2)- escrita (3)- configuração? (4)- sair?: \n\r")

                if sel == '1':
                    tipo = input (f"Qual tipo de dado deseja ler? 1-holding register 2- Coil 3- Input Reg 4- Discrete Input :")
                    addr = input("Digite o endereço da tabela MODBUS: ")
                    nvezes = input("Quantas vezes deseja ler? ")
                    for i in range(0,int(nvezes)):
                        print(f"Leitura {i+1}: {self.lerDado(int(tipo),int(addr))}")
                        sleep(self._scan_time)

                elif sel == '2':
                    tipo = input (f"Qual tipo de dado deseja escrever? 1-holding register 2- Coil :")
                    addr = input("Digite o endereço da tabela MODBUS: ")                
                    valor = input("Digite o valor a ser escrito: ")
                    self.escreveDado(int(tipo), int(addr), int(valor))

                elif sel == '3':
                    scanTime = input("Qual o tempo de varredura desejado [s]?:")
                    self._scan_time = float(scanTime)

                elif sel == '4':
                    self._client.close()
                    atendimento = False
                
                else:
                    print("Seleção Inválida")

        except Exception as e:
            print("Error: ", e.args)
    


    def lerDado(self,tipo, addr):
        #método para leitura de dado na tabela MODBUS
        if tipo == 1:
            return self._client.read_holding_registers(addr, 1)[0]
            
        if tipo == 2:
            return self._client.read_coils(addr, 1)[0]
        
        if tipo == 3:
            return self._client.read_holding_registers(addr, 1)[0]
        
        if tipo == 4:
            return self._client.read_discrete_inputs(addr, 1)[0]

    
    def escreveDado(self, tipo, addr, valor):
        #metodo para a escrita de dados na tabela MODBUS
        if tipo == 1:
            return self._client.write_single_register(addr, valor)
            
        if tipo == 2:
            return self._client.write_single_coil(addr, valor)
