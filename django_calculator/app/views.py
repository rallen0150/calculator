from django.shortcuts import render

# Create your views here.
def choice(a, b, c):
    if c == '+':
        return int(a)+int(b)
    elif c == '-':
        return int(a)-int(b)
    elif c == '*':
        return int(a)*int(b)
    elif c == '/':
        if b == '0':
            return "Can't Divide by 0"
        else:
            return int(a)/int(b)


def index_view(request):
    answer = request.GET
    if request.GET:
        num1 = answer['number1']
        num2 = answer['number2']
        operator = answer['choice']
        print(request.GET)
    else:
        num1=0
        num2=0
        operator='+'

    context = {
        "number1": num1,
        "number2": num2,
        "choice": operator,
        "math_eq": choice(num1, num2, operator)
    }

    return render(request, "index.html", context)
