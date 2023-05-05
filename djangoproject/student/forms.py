from django.forms import ModelForm
from django import forms
from .models import File


class UploadForm(ModelForm):
    subject = forms.ChoiceField(label = 'Matéria', choices=(('mat', 'Matemática'), ('port', 'Português')))
    school = forms.ChoiceField(label = 'Escola', choices=(('GP', 'Escola1'), ('MS', 'Escola2')))
    sex = forms.ChoiceField(label = 'Gênero', choices=(('F', 'Feminino'), ('M', 'Masculino'), ('O', 'Outros')))
    age = forms.IntegerField(label = 'Idade')
    adress = forms.ChoiceField(label = 'Residência', choices=(('U', 'Urbano'), ('R', 'Rural')))
    famsize = forms.IntegerField(label = 'Tamanho da Família')
    Pstatus = forms.ChoiceField(label = 'Relacionamento dos pais', choices=(('T', 'Casados'), ('A', 'Divorciados')))
    Medu = forms.ChoiceField(label = 'Educação da mãe', choices=(
    (1, 'Fundamental I Incompleto'), (2, 'Fundamental I Completo'), (3, 'Fundamental II Completo '),
    (4, 'Ensino Médio Completo')))
    Fedu = forms.ChoiceField(label = 'Educação do pai', choices=(
    (1, 'Fundamental I Incompleto'), (2, 'Fundamental I Completo'), (3, 'Fundamental II Completo '),
    (4, 'Ensino Médio Completo')))
    guardian = forms.ChoiceField(label = 'Guardião', choices=(('mother', 'Mãe'), ('father', 'Pai'), ('other', 'Outro')))
    traveltime = forms.ChoiceField(label = 'Tempo para chegar à escola',
        choices=((1, '< 15 min.'), (2, '15 min. - 30 min.'), (3, '30 min. - 1 hr'), (4, '> 1 hr')))
    studytime = forms.ChoiceField(label = 'Tempo semanal de estudo',
        choices=((1, '< 2 hrs'), (2, '2 hrs - 5 hrs'), (3, '5 hrs - 10 hrs'), (4, '> 10 hrs')))
    failures = forms.IntegerField(label = 'Reprovações')
    schoolsup = forms.ChoiceField(label = 'Reforço escolar', choices=(('yes', 'Sim'), ('no', 'Não')))
    famsup = forms.ChoiceField(label = 'Apoio da família', choices=(('yes', 'Sim'), ('no', 'Não')))
    paid = forms.ChoiceField(label = 'Pagante', choices=(('yes', 'Sim'), ('no', 'Não')))
    activities = forms.ChoiceField(label = 'Atividades extra classe', choices=(('yes', 'Sim'), ('no', 'Não')))
    internet = forms.ChoiceField(label = 'Acesso à internet', choices=(('yes', 'Sim'), ('no', 'Não')))
    famrel = forms.ChoiceField(label = 'Relacionamento com a família', choices=((1, 'Muito ruim'), (2, 'Ruim'), (3, 'Normal'), (4, 'Boa'), (5, 'Muito boa')))
    freetime = forms.ChoiceField(label = 'Tempo livre',
        choices=((1, 'Muito pouco'), (2, 'Pouco'), (3, 'Razoável'), (4, 'Alto'), (5, 'Muito alto')))
    goout = forms.ChoiceField(label = 'Tempo de saída com amigos',
        choices=((1, 'Muito pouco'), (2, 'Pouco'), (3, 'Razoável'), (4, 'Alto'), (5, 'Muito alto')))
    Dalc = forms.ChoiceField(label = 'Consumo de álcool',
        choices=((1, 'Muito pouco'), (2, 'Pouco'), (3, 'Razoável'), (4, 'Alto'), (5, 'Muito alto')))
    health = forms.ChoiceField(label = 'Condição de saúde', choices=((1, 'Muito ruim'), (2, 'Ruim'), (3, 'Normal'), (4, 'Boa'), (5, 'Muito boa')))
    absences = forms.IntegerField(label = 'Faltas')
    G1 = forms.IntegerField(label='Nota da P1')
    G2 = forms.IntegerField(label='Nota da P2')
    G3 = forms.IntegerField(label='Nota da P3')

    class Meta:
        model = File
        fields = ["subject","school","sex","age","adress","famsize","Pstatus","Medu","Fedu","guardian","traveltime","studytime","failures","schoolsup","famsup","paid","activities","internet","famrel","freetime","goout","Dalc","health","absences","G1","G2","G3"]
