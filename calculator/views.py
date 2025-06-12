from django.shortcuts import render, redirect
from .forms import MathForm

def home_redirect(request):
    return redirect('form')

def calculate_view(request):
    result = None
    error = None

    if request.method == 'POST':
        form = MathForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['input1']
            b = form.cleaned_data['input2']
            op = form.cleaned_data['operation']

            if op == 'add':
                result = a + b
            elif op == 'sub':
                result = a - b
            elif op == 'mul':
                result = a * b
            elif op == 'div':
                if b != 0:
                    result = a / b
                else:
                    error = "Error: Division by zero"

            if error is None:
                if result > 100:
                    result *= 2
                elif result < 0:
                    result += 50

        else:
            error = "Invalid input."

    else:
        form = MathForm()

    if error:
        return render(request, 'calculator/math_form.html', {'form': form, 'error': error})

    if result is not None:
        return render(request, 'calculator/result.html', {'result': result})

    return render(request, 'calculator/math_form.html', {'form': form})

