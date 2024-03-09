class Professional():
    def __init__(self, nome, especialidade, CRM):
        self.nome = nome
        self.especialidade = especialidade
        self.CRM = CRM

    def imprimir_info(self):
        print('nome: {} especialidade: {} CRM: {}'.format(self.nome, self.especialidade, self.CRM))

class Medico(Professional):

    def agendamento(self):
        print("Medico " + self.nome + " agendou uma consulta")
        
    def imprimir_info(self):
        print('Reescrevendo do metodo filho')

profissional = Professional('Fernando', 'Clínico', '654321')
profissional.imprimir_info()

medico = Medico('Carol', 'oftalmo', '123456')
medico.imprimir_info()

# #-----------------------------------------------------------------------------------//------------------------------
# class Professional():
#     def __init__(self, nome, especialidade, CRM):
#         self.nome = nome
#         self.especialidade = especialidade
#         self.CRM = CRM

# class Medico(Professional):
#     def __init__(self, nome, especialidade, CRM):
#         super().__init__(nome, especialidade, CRM)

#     def agendamento(self):
#         print("Médico " + self.nome + " agendou uma consulta")

# profissional = Medico('Fernando', 'Clínico', '654321')
# profissional.agendamento()
