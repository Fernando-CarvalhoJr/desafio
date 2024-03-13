class Pessoa:
    def __init__(self, nome):
        self.nome = nome

class Funcionario(Pessoa):
    def __init__(self, nome, especialidade):
        super().__init__(nome)
        self.especialidade = especialidade

class Paciente(Pessoa):
    def __init__(self, nome):
        super().__init__(nome)

class Medico(Funcionario):
    def __init__(self, nome, especialidade, CRM):
        super().__init__(nome, especialidade)
        self.CRM = CRM

    def consulta(self, paciente, data):
        print('Dr. {} realizou um agendamento para o paciente {} no dia {}'.format(self.nome, paciente, data))

    def exame(self, paciente, tipo_exame):
        print('Dr. {} realizou uma {} no paciente {}'.format(self.nome, tipo_exame, paciente))

    def prescrever_medicamento(self, paciente, remedio):
        print('Dr. {} prescreveu {} para o paciente {}'.format(self.nome, remedio, paciente))

class Enfermeiro(Funcionario):
    def __init__(self, nome, especialidade, coren):
        super().__init__(nome, especialidade)
        self.coren = coren

    def injecao(self, paciente):
        print('Enf. {} aplicou injeção no paciente {}'.format(self.nome, paciente))

    def consulta(self, paciente, data):
        print('Enf. {} realizou um agendamento para o paciente {} no dia {}'.format(self.nome, paciente, data))


# Exemplo de uso
medico = Medico("Gabriel", "Ortopedista", "12345")
enfermeiro = Enfermeiro("Jamily", "Clínica Geral", "54321")
paciente = Paciente("Fernando")

medico.consulta(paciente.nome, "10/03/2024")
enfermeiro.injecao(paciente.nome)
medico.exame(paciente.nome, "Raio X")
enfermeiro.consulta(paciente.nome, "15/03/2024")
medico.prescrever_medicamento(paciente.nome, "Dorflex")

