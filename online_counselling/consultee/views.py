from django.shortcuts import render, HttpResponse, redirect
from .forms import ConsulteeForm
from consultant.forms import UserForm
from administration.models import UserRole
from consultant.models import Consultant

import pandas as pd
from sklearn.preprocessing import OrdinalEncoder, OneHotEncoder
import joblib

# Create your views here.
def demo(request):
    return HttpResponse('In Consultee')


def register_consultee(request):
    if request.method == 'GET':
        user_form = UserForm()
        consultee_form = ConsulteeForm()
        context = {}
        context['user_form'] = user_form
        context['consultee_form'] = consultee_form
        return render(request, 'consultee/registeration-form.html', context)
    else:
        user_form = UserForm(request.POST)
        consultee_form = ConsulteeForm(request.POST)
        user_role = UserRole()
        context = {}
        context['user_form'] = user_form
        context['consultee_form'] = consultee_form
        if user_form.is_valid() and consultee_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            user_role.user = user
            user_role.role = 'Consultee'
            user_role.save()
            consultee = consultee_form.save(commit=False)
            consultee.user = user
            consultee.ratings = 0
            consultee.number_of_reviews = 0
            consultee.number_of_customers = 0
            consultee.save()
            return redirect('login_user')
        else:
            return render(request, 'consultee/registeration-form.html', context)


def view_consultant(request, pk):
    consultant = Consultant.objects.get(id=pk)
    id = pk
    data = pd.read_csv('database_data.csv')
    data = data.drop('Unnamed: 0', axis=1)
    data = data.set_index('id')
    print(data)
    encoder = OrdinalEncoder()
    xy = encoder.fit_transform(data['type_of_consultant'].values.reshape(-1,1))
    he = OneHotEncoder()
    ab = he.fit_transform(xy).toarray()
    data[['Career', 'Doctor', 'Education', 'Lawyer']] = ab
    X = data.iloc[:, [4, 5, 6, 12, 13, 14, 15, 16, 17]]
    y = pd.DataFrame([0 for i in range(2006)])
    X_predict = X.iloc[id-1:id, :]
    print(X_predict)
    model = joblib.load('model_final.sav')
    result = model.kneighbors(X_predict, n_neighbors=10)
    ids = list(map(int, result[1].reshape(-1, 1)))
    print(X.iloc[list(map(int, result[1].reshape(-1, 1))), :])
    consultant_rec = []
    for id in ids:
        consultant_temp = Consultant.objects.get(id=id+1)
        consultant_rec.append(consultant_temp)
        print('___', consultant_temp.id)
    print(dir(consultant_rec[0]))
    return render(request, 'consultee/viewConsultant.html', {'consultant': consultant, 'consultant_rec': consultant_rec})
