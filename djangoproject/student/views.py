from django.shortcuts import render, redirect, get_object_or_404, reverse
from .models import File
from django.views.generic import View
import pandas as pd
import plotly.express as px
from plotly.offline import plot
from .forms import UploadForm
from django.http import HttpResponse

class HomeView(View):  # definimos a classe HomeView que será nossa página principal
    def get(self, request, *args,
            **kwargs):  # esta classe fará que, quando requisitada (pela homepage da nossa aplicação web) seja renderizado o index.html (que está dentro de student)
        return render(request, 'student/index.html') #esta classe irá chamar o arquivo index.html

class DescriptiveView(View):  # definimos a classe DescriptiveView que abrirá os gráficos com a descrição dos alunos
    def get(self, request, *args,
            **kwargs):  # esta classe fará que, quando requisitada (pela homepage da nossa aplicação web) seja renderizado o descriptive.html.html (que está dentro de student)
        data = File.objects.all()
        chart = [
            {
                'subject': x.subject,
                'sex': x.sex,
                'age': x.age,
                'adress': x.adress,
                'famsize': x.famsize,
                'guardian': x.guardian,
                'traveltime': x.traveltime,
                'studytime': x.studytime,
                'paid': x.paid,
                'internet': x.internet,
                'freetime': x.freetime,
                'Dalc': x.Dalc,
                'absences': x.absences
            }for x in data
        ]
        df = pd.DataFrame(chart)

        #definir estrutura de dados
        #contagem de alunos por matéria
        alunos_mat = df.groupby(['subject']).count()['age'].reset_index()
        alunos_sex = df.groupby(['sex']).count()['age'].reset_index()
        alunos_age = df.groupby(['age']).count()['sex'].reset_index()
        alunos_guardian = df.groupby(['guardian']).count()['sex'].reset_index()
        alunos_adress = df.groupby(['adress']).count()['sex'].reset_index()

        labels = {'port': 'Português', 'mat': 'Matemática'}
        alunos_mat['subject'] = alunos_mat['subject'].map(labels)

        pie = px.pie(alunos_mat, values='age', names='subject', title='Proporção de alunos por matéria',
                     labels={
                         'age': 'Número de alunos',
                         "subject": 'Matéria'
                     },
                     color_discrete_sequence=px.colors.qualitative.Antique
                     )



        pie2 = px.pie(alunos_age, values='sex', names='age', title='Proporção de alunos por idade',
                     labels={
                         'sex': 'Número de alunos',
                         "age": 'Idade'
                     },
                     color_discrete_sequence=px.colors.qualitative.Antique
                     )

        labels = {'F': 'Feminino', 'M': 'Masculino'}
        alunos_sex['sex'] = alunos_sex['sex'].map(labels)

        pie3 = px.pie(alunos_sex, values='age', names='sex', title='Proporção de alunos por gênero',
                     labels={
                         'age': 'Número de alunos',
                         "sex": 'Matéria'
                     },
                     color_discrete_sequence=px.colors.qualitative.Antique
                     )

        labels = {'mother': 'Mãe', 'father': 'Pai', 'other': 'Outros'}
        alunos_guardian['guardian'] = alunos_guardian['guardian'].map(labels)

        pie4 = px.pie(alunos_guardian, values='sex', names='guardian', title='Proporção de alunos por guardião',
                     labels={
                         'sex': 'Número de alunos',
                         "guardian": 'Guardião'
                     },
                     color_discrete_sequence=px.colors.qualitative.Antique
                     )

        labels = {'U': 'Urbano', 'R': 'Rural'}
        alunos_adress['adress'] = alunos_adress['adress'].map(labels)

        pie5 = px.pie(alunos_adress, values='sex', names='adress', title='Proporção de alunos por moradia',
                     labels={
                         'sex': 'Número de alunos',
                         "adress": 'Moradia'
                     },
                     color_discrete_sequence=px.colors.qualitative.Antique
                     )

        fig1 = plot(pie, output_type='div')
        fig2 = plot(pie2, output_type='div')
        fig3 = plot(pie3, output_type='div')
        fig4 = plot(pie4, output_type='div')
        fig5 = plot(pie5, output_type='div')

        ctx ={'fig1': fig1, 'fig2': fig2, 'fig3': fig3, 'fig4': fig4, 'fig5': fig5}

        return render(request, 'student/descriptive.html', ctx) #esta classe irá chamar o arquivo descriptive.html

class HabitsView(View):  # definimos a classe ModellingView que abrirá os gráficos com algumas modelagens de dados
    def get(self, request, *args,
            **kwargs):  # esta classe fará que, quando requisitada (pela homepage da nossa aplicação web) seja renderizado o habits.html (que está dentro de irisjs)

        data = File.objects.all()
        chart = [
            {
                'subject': x.subject,
                'sex': x.sex,
                'age': x.age,
                'adress': x.adress,
                'famsize': x.famsize,
                'guardian': x.guardian,
                'traveltime': x.traveltime,
                'studytime': x.studytime,
                'paid': x.paid,
                'internet': x.internet,
                'freetime': x.freetime,
                'Dalc': x.Dalc,
                'absences': x.absences
            }for x in data
        ]
        df = pd.DataFrame(chart)

        alunos_trav = df.groupby(['traveltime']).count()['age'].reset_index()
        alunos_stud = df.groupby(['studytime']).count()['age'].reset_index()
        alunos_free = df.groupby(['freetime']).count()['age'].reset_index()
        alunos_alc = df.groupby(['Dalc']).count()['age'].reset_index()


        bar = px.bar(alunos_trav, x="traveltime", y="age",
                      title="Tempo gasto para chegar à escola",
                     labels = {
                         "traveltime": "Tempo do trajeto",
                         "age": "Número de alunos"
                     }, color_discrete_sequence=px.colors.qualitative.Antique
                     )

        bar.update_layout(
            xaxis=dict(
                tickmode='array',
                tickvals=[1, 2, 3, 4],
                ticktext=['<15 min', '15 - 30 min.', '30 min. - 1h', '> 1h']
            )
        )

        bar2 = px.bar(alunos_stud, x="studytime", y="age",
                      title="Tempo de estudo por semana",
                     labels = {
                         "studytime": "Tempo de estudo",
                         "age": "Número de alunos"
                     }, color_discrete_sequence=px.colors.qualitative.Antique
                     )

        bar2.update_layout(
            xaxis=dict(
                tickmode='array',
                tickvals=[1, 2, 3, 4],
                ticktext=['< 2h', '2h - 5h', '5h - 10h', '> 10h']
            )
        )

        bar3 = px.bar(alunos_free, x="freetime", y="age",
                      title="Tempo de livre após a escola",
                     labels = {
                         "freetime": "Tempo livre",
                         "age": "Número de alunos"
                     }, color_discrete_sequence=px.colors.qualitative.Antique
                     )

        bar3.update_layout(
            xaxis=dict(
                tickmode='array',
                tickvals=[1, 2, 3, 4, 5],
                ticktext=['Muito pouco', 'Pouco', 'Moderado', 'Alto', 'Muito Alto']
            )
        )

        bar4 = px.bar(alunos_alc, x="Dalc", y="age",
                      title="Consumo de álcool durante a semana",
                     labels = {
                         "Dalc": "Consumo de álcool",
                         "age": "Número de alunos"
                     }, color_discrete_sequence=px.colors.qualitative.Antique
                     )

        bar4.update_layout(
            xaxis=dict(
                tickmode='array',
                tickvals=[1, 2, 3, 4, 5],
                ticktext=['Muito pouco', 'Pouco', 'Moderado', 'Alto', 'Muito Alto']
            )
        )

        fig1 = plot(bar, output_type='div')
        fig2 = plot(bar2, output_type='div')
        fig3 = plot(bar3, output_type='div')
        fig4 = plot(bar4, output_type='div')

        ctx = {'fig1': fig1, 'fig2': fig2, 'fig3': fig3, 'fig4': fig4}

        return render(request, 'student/habits.html',ctx) #esta classe irá chamar o arquivo habits.html

class ModellingView(View):  # definimos a classe ModellingView que abrirá os gráficos com algumas modelagens de dados
    def get(self, request, *args,
            **kwargs):  # esta classe fará que, quando requisitada (pela homepage da nossa aplicação web) seja renderizado o habits.html (que está dentro de irisjs)

        data = File.objects.all()
        chart = [
            {
                'subject': x.subject,
                'sex': x.sex,
                'age': x.age,
                'adress': x.adress,
                'famsize': x.famsize,
                'guardian': x.guardian,
                'traveltime': x.traveltime,
                'studytime': x.studytime,
                'paid': x.paid,
                'internet': x.internet,
                'freetime': x.freetime,
                'Dalc': x.Dalc,
                'absences': x.absences,
                'G1': x.G1,
                'G2': x.G2,
                'G3': x.G3
            }for x in data
        ]
        df = pd.DataFrame(chart)

        G4 = (df.G1 + df.G2 + df.G3)/3

        df['G4'] = G4

        scat = px.scatter(df[df['subject'] == 'port'], x='absences', y='G4',
                          title = 'Média das notas de português em relação às faltas',
                          labels = {
                              'absences': 'Faltas',
                              'G4': 'Média das notas em português'

                          }, color_discrete_sequence=px.colors.qualitative.Antique)

        scat2 = px.scatter(df[df['subject'] == 'mat'], x='absences', y='G4',
                          title = 'Média das notas de matemática em relação às faltas',
                          labels = {
                              'absences': 'Faltas',
                              'G4': 'Média das notas em matemática'

                          }, color_discrete_sequence=px.colors.qualitative.Pastel)

        box = px.box(df[df['subject'] == 'port'], x='traveltime', y='G4',
                          title = 'Média das notas de português em relação ao tempo do trajeto',
                          labels = {
                              'traveltime': 'Tempo do trajeto',
                              'G4': 'Média das notas em português'

                          }, color_discrete_sequence=px.colors.qualitative.Antique)

        box.update_layout(
            xaxis=dict(
                tickmode='array',
                tickvals=[1, 2, 3, 4],
                ticktext=['<15 min', '15 - 30 min.', '30 min. - 1h', '> 1h']
            )
        )

        box2 = px.box(df[df['subject'] == 'mat'], x='traveltime', y='G4',
                          title = 'Média das notas de matemática em relação ao tempo do trajeto',
                          labels = {
                              'traveltime': 'Tempo do trajeto',
                              'G4': 'Média das notas em matemática'

                          }, color_discrete_sequence=px.colors.qualitative.Pastel)

        box2.update_layout(
            xaxis=dict(
                tickmode='array',
                tickvals=[1, 2, 3, 4],
                ticktext=['<15 min', '15 - 30 min.', '30 min. - 1h', '> 1h']
            )
        )

        box3 = px.box(df[df['subject'] == 'port'], x='studytime', y='G4',
                          title = 'Média das notas de português em relação ao tempo do estudo',
                          labels = {
                              'studytime': 'Tempo de estudo semanal',
                              'G4': 'Média das notas em português'

                          }, color_discrete_sequence=px.colors.qualitative.Antique)

        box3.update_layout(
            xaxis=dict(
                tickmode='array',
                tickvals=[1, 2, 3, 4],
                ticktext=['< 2h', '2h - 5h', '5h - 10h', '> 10h']
            )
        )

        box4 = px.box(df[df['subject'] == 'mat'], x='studytime', y='G4',
                          title = 'Média das notas de matemática em relação ao tempo do estudo',
                          labels = {
                              'studytime': 'Tempo de estudo semanal',
                              'G4': 'Média das notas em matemática'

                          }, color_discrete_sequence=px.colors.qualitative.Pastel)

        box4.update_layout(
            xaxis=dict(
                tickmode='array',
                tickvals=[1, 2, 3, 4],
                ticktext=['< 2h', '2h - 5h', '5h - 10h', '> 10h']
            )
        )

        box5 = px.box(df[df['subject'] == 'port'], x='Dalc', y='G4',
                          title = 'Média das notas de português em relação ao consumo de álcool',
                          labels = {
                              'Dalc': 'Consumo de álcool',
                              'G4': 'Média das notas em português'

                          }, color_discrete_sequence=px.colors.qualitative.Antique)

        box5.update_layout(
            xaxis=dict(
                tickmode='array',
                tickvals=[1, 2, 3, 4, 5],
                ticktext=['Muito pouco', 'Pouco', 'Moderado', 'Alto', 'Muito Alto']
            )
        )

        box6 = px.box(df[df['subject'] == 'mat'], x='Dalc', y='G4',
                          title = 'Média das notas de matemática em relação ao consumo de álcool',
                          labels = {
                              'Dalc': 'Consumo de álcool',
                              'G4': 'Média das notas em mtemática'

                          }, color_discrete_sequence=px.colors.qualitative.Pastel)

        box6.update_layout(
            xaxis=dict(
                tickmode='array',
                tickvals=[1, 2, 3, 4, 5],
                ticktext=['Muito pouco', 'Pouco', 'Moderado', 'Alto', 'Muito Alto']
            )
        )

        fig1 = plot(scat, output_type='div')
        fig2 = plot(scat2, output_type='div')
        fig3 = plot(box, output_type='div')
        fig4 = plot(box2, output_type='div')
        fig5 = plot(box3, output_type='div')
        fig6 = plot(box4, output_type='div')
        fig7 = plot(box5, output_type='div')
        fig8 = plot(box6, output_type='div')

        ctx = {'fig1': fig1, 'fig2': fig2, 'fig3': fig3, 'fig4': fig4, 'fig5': fig5, 'fig6': fig6, 'fig7': fig7,'fig8':fig8}

        return render(request, 'student/modelling.html', ctx)


def home(request):
    return HttpResponse('ok')

def upload(request):
    if request.POST:
        form = UploadForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect(home)
    return render(request, 'student/upload.html', {'form': UploadForm})