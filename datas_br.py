from datetime import datetime, timedelta

class DatasBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()
    def __str__(self):
        return self.format_data()
    def mes_cadastro(self):
        meses_ano = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                     'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
        mes_cadastro = self.momento_cadastro.month
        return meses_ano[mes_cadastro-1]
    def dia_semana(self):
        dias_semana = ['Segunda', 'Terça', 'Quarta','Quinta',
                       'Sexta', 'Sábado', 'Domingo']
        dia_semana = self.momento_cadastro.weekday()
        return dias_semana[dia_semana]
    def format_data(self):
        data_formatada = self.momento_cadastro.strftime('%d/%m/%Y %H:%M')
        return data_formatada
    def tempo_cadastro(self):
        tempo_cadastro = datetime.today() + timedelta(days=1, hours=23) - self.momento_cadastro
        return tempo_cadastro


