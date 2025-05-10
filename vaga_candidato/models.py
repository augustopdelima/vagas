from django.db import models

AREA_CHOICES = {
    "Ti": "Tecnologia da Informação",
    "Rh": "Recursos Humanos",
    "Fi": "Financeiro",
    "Tr": "Transporte"
}

TIPO_CONTRATO_CHOICES = {
    "CLT": "Consolidação das Leis do Trabalho",
    "PJ": "Pessoa Jurídica",
    "MEI": "Microempreendedor",
    "COO": "Cooperado"
}

GENERO_CHOICES = {
    "Ma": "Masculino",
    "Fe": "Feminino",
    "Nb": "Não Binário",
    "Ou": "Outros"
}

ESCOLARIDADE_CHOICES = {
    "FUN": "Fundamental",
    "MED": "Médio",
    "SUP": "Superior",
    "POS": "Pós-graduação",
    "MES": "Mestrado",
    "DOU": "Doutorado"
}


class Vaga(models.Model):
    titulo = models.CharField(max_length=63, verbose_name="Título")

    area = models.CharField(
        max_length=2, choices=AREA_CHOICES, verbose_name="Área")

    tipo_contrato = models.CharField(
        max_length=3, verbose_name="Tipo de contrato", choices=TIPO_CONTRATO_CHOICES)

    descricao = models.TextField(max_length=255, verbose_name="Descrição")

    def __str__(self):
        return f'{self.area}:{self.titulo}:{self.tipo_contrato}'


class Candidato(models.Model):
    nome = models.CharField(max_length=31, verbose_name="Nome")

    sobrenome = models.CharField(max_length=31, verbose_name="Sobrenome")

    data_nascimento = models.DateField(verbose_name="Data de nascimento")

    genero = models.CharField(
        max_length=2, verbose_name="Gênero", choices=GENERO_CHOICES)

    email = models.EmailField(verbose_name="Email")

    telefone = models.CharField(max_length=10, verbose_name="Telefone")

    escolaridade = models.CharField(
        max_length=63, verbose_name="Escolaridade", choices=ESCOLARIDADE_CHOICES)

    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE)

    def __srt__(self):
        return f'{self.nome} {self.sobrenome}'
