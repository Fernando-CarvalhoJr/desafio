class Professional():
    def __init__(self, nome, especialidade, CRM):
        self.nome = nome
        self.especialidade = especialidade
        self.CRM = CRM

    def imprimir_info(self):
        print("""-- Nome: {}\n
-- Especialidade: {}""".format(self.nome, self.especialidade))

class Medico(Professional):

    def agendamento(self):
        print("Medico " + self.nome + " agendou uma consulta")
        
    def imprimir_info(self):
        print("""\n-- Nome: {} \n
-- Especialidade: {} \n
-- CRM: {}\n""".format(self.nome, self.especialidade, self.CRM))
        
class Enfermeiro(Professional)

profissional = Professional('Fernando', 'Clínico', '654321')
profissional.imprimir_info()

medico = Medico('Carol', 'oftalmo', '123456')
medico.imprimir_info()
medico.agendamento()

