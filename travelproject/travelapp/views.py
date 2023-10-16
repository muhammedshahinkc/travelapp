from django.shortcuts import render

# def demo(request):
#
#     return render(request,"demo.html", )
# def addition(request):
#     x=int(request.GET["num1"])
#     y=int(request.GET["num2"])
#     res=x+y
#     sub=x-y
#     mul=x*y
#     div=x/y
#     return render(request,"add.html",{"result":res,"substraction":sub,"multiplication":mul,"division":div})

def demo(request):

    return render(request,"index.html", )