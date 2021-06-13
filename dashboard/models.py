from django.db import models

# Create your models here.

class CampeonatoConstrutores(models.Model):
    id_campeonato_construtores = models.IntegerField(primary_key=True)
    id_corrida = models.ForeignKey('Corridas', models.DO_NOTHING, db_column='id_corrida', blank=True, null=True)
    id_construtor = models.ForeignKey('Construtores', models.DO_NOTHING, db_column='id_construtor', blank=True, null=True)
    pontos = models.FloatField()
    posicao = models.IntegerField(blank=True, null=True)
    texto_posicao = models.CharField(max_length=50, blank=True, null=True)
    wins = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'campeonato_construtores'


class CampeonatoPilotos(models.Model):
    id_campeonato_pilotos = models.IntegerField(primary_key=True)
    id_corrida = models.ForeignKey('Corridas', models.DO_NOTHING, db_column='id_corrida', blank=True, null=True)
    id_piloto = models.ForeignKey('Pilotos', models.DO_NOTHING, db_column='id_piloto', blank=True, null=True)
    pontos = models.FloatField()
    posicao = models.IntegerField(blank=True, null=True)
    texto_posicao = models.CharField(max_length=50, blank=True, null=True)
    wins = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'campeonato_pilotos'


class Circuitos(models.Model):
    id_circuito = models.IntegerField(primary_key=True)
    ref_circuito = models.CharField(max_length=100)
    nome_circuito = models.CharField(max_length=100)
    location_circuito = models.CharField(max_length=100)
    pais_circuito = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'circuitos'


class Classificacao(models.Model):
    id_classificacao = models.IntegerField(primary_key=True)
    id_corrida = models.ForeignKey('Corridas', models.DO_NOTHING, db_column='id_corrida')
    id_piloto = models.ForeignKey('Pilotos', models.DO_NOTHING, db_column='id_piloto')
    id_construtor = models.ForeignKey('Construtores', models.DO_NOTHING, db_column='id_construtor')
    numero = models.IntegerField()
    posicao = models.IntegerField(blank=True, null=True)
    q1 = models.CharField(max_length=50, blank=True, null=True)
    q2 = models.CharField(max_length=50, blank=True, null=True)
    q3 = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'classificacao'


class Construtores(models.Model):
    id_construtor = models.IntegerField(primary_key=True)
    nome_construtor = models.CharField(max_length=50)
    nacionalidade_construtor = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'construtores'


class Corridas(models.Model):
    id_corrida = models.IntegerField(primary_key=True)
    ano_corrida = models.ForeignKey('Temporadas', models.DO_NOTHING, db_column='ano_corrida')
    rodada = models.IntegerField()
    id_circuito = models.ForeignKey(Circuitos, models.DO_NOTHING, db_column='id_circuito')
    nome_corrida = models.CharField(max_length=100)
    data_corrida = models.DateField()
    tempo_corrida = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'corridas'


class Laptime(models.Model):
    id_corrida = models.OneToOneField(Corridas, models.DO_NOTHING, db_column='id_corrida', primary_key=True)
    id_piloto = models.ForeignKey('Pilotos', models.DO_NOTHING, db_column='id_piloto')
    lap = models.IntegerField()
    posicao = models.IntegerField(blank=True, null=True)
    tempo = models.CharField(max_length=50, blank=True, null=True)
    milisegundos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'laptime'
        unique_together = (('id_corrida', 'id_piloto', 'lap'),)


class Pilotos(models.Model):
    id_piloto = models.IntegerField(primary_key=True)
    ref_piloto = models.CharField(max_length=50)
    code_piloto = models.CharField(max_length=5, blank=True, null=True)
    primeiro_nome = models.CharField(max_length=50)
    ultimo_nome = models.CharField(max_length=50)
    nascimento = models.DateField(blank=True, null=True)
    nacionalidade_piloto = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pilotos'


class Pitstop(models.Model):
    id_corrida = models.OneToOneField(Corridas, models.DO_NOTHING, db_column='id_corrida', primary_key=True)
    id_piloto = models.ForeignKey(Pilotos, models.DO_NOTHING, db_column='id_piloto')
    parada = models.IntegerField()
    volta = models.IntegerField()
    tempo = models.TimeField()
    duracao = models.CharField(max_length=50, blank=True, null=True)
    milisegundos = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pitstop'
        unique_together = (('id_corrida', 'id_piloto', 'parada'),)


class ResultadoConstrutores(models.Model):
    id_resultado_construtor = models.IntegerField(primary_key=True)
    id_corrida = models.ForeignKey(Corridas, models.DO_NOTHING, db_column='id_corrida', blank=True, null=True)
    id_construtor = models.ForeignKey(Construtores, models.DO_NOTHING, db_column='id_construtor', blank=True, null=True)
    pontos = models.FloatField(blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'resultado_construtores'


class Resultados(models.Model):
    id_resultado = models.IntegerField(primary_key=True)
    id_corrida = models.ForeignKey(Corridas, models.DO_NOTHING, db_column='id_corrida')
    id_piloto = models.ForeignKey(Pilotos, models.DO_NOTHING, db_column='id_piloto')
    id_construtor = models.ForeignKey(Construtores, models.DO_NOTHING, db_column='id_construtor')
    numero = models.IntegerField()
    grid = models.IntegerField()
    posicao = models.IntegerField(blank=True, null=True)
    texto_posicao = models.CharField(max_length=10)
    ordem_posicao = models.IntegerField()
    pontos = models.FloatField()
    voltas = models.IntegerField()
    tempo = models.CharField(max_length=50, blank=True, null=True)
    milisegundos = models.IntegerField(blank=True, null=True)
    voltarapida = models.IntegerField(blank=True, null=True)
    ranking = models.IntegerField(blank=True, null=True)
    tempo_volta = models.CharField(max_length=50, blank=True, null=True)
    tempo_voltarapida = models.CharField(max_length=50, blank=True, null=True)
    id_status = models.ForeignKey('Status', models.DO_NOTHING, db_column='id_status')

    class Meta:
        managed = False
        db_table = 'resultados'


class Status(models.Model):
    id_status = models.IntegerField(primary_key=True)
    descricao_status = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'status'


class Temporadas(models.Model):
    ano = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'temporadas'
    

