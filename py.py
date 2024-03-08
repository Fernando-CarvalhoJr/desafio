    class Professional():
        def __init__(self, nome, especialidade, CRM):
            self.nome = nome
            self.especialidade = especialidade
            self.CRM = CRM

    class Medico(Professional):

        def agendamento(self):
            print("Medico " + self.nome + " agendou uma consulta")

        def imprimir_info(self):
            print('nome do medico: ', self.nome)
            print('especialidade do medico:', self.especialidade)
            print('numero do CRM: ', self.CRM)

    profissional = Professional('Fernando', 'Clínico', '654321')
    profissional.imprimir_info()



#-----------------------------------------------------------------------------------//------------------------------
class Professional():
    def __init__(self, nome, especialidade, CRM):
        self.nome = nome
        self.especialidade = especialidade
        self.CRM = CRM

class Medico(Professional):
    def __init__(self, nome, especialidade, CRM):
        super().__init__(nome, especialidade, CRM)

    def agendamento(self):
        print("Médico " + self.nome + " agendou uma consulta")

profissional = Medico('Fernando', 'Clínico', '654321')
profissional.agendamento()
