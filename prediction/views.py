from django.shortcuts import render

# Create your views here.
def home(request) :
    context={'message' : "어획량 예측 서비스"}
    return render(request, 'prediction/home.html', context)