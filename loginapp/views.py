from django.shortcuts import render

# from project2.loginapp import LoginForm


def loginreq(request):


    if request.method == "POST":
        get_uname=request.POST.get("uname")
        return render(request, 'Templates/loggedin.html', {"username": get_uname})




    def loginform(request):
        if request.method=="GET":
            return render(request, "Templates/signup.html")

