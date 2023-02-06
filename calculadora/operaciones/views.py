from django.shortcuts import render


def math_operation(request):
    operator = request.GET.get('operator')
    if request.GET.get('operand1') == None and request.GET.get('operand2') == None:
        return render(request, 'operaciones/math_operation.html', {
            'result': None})
    try:
        operand1 = float(request.GET.get('operand1'))
        operand2 = float(request.GET.get('operand2'))
    except:
        result = 'Entrada no valida'
        return render(request, 'operaciones/math_operation.html', {
            'result': result,
            'operand1': request.GET.get('operand1'),
            'operand2': request.GET.get('operand2'),
            'operator':operator
        })
    result = None

    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        if (operand2 == 0):
            result = 'No se admite división entre 0'
        else:
            result = operand1 / operand2
    else:
        result = 'Operador no valido'

    return render(request, 'operaciones/math_operation.html', {
            'result': result,
            'operand1': operand1,
            'operand2': operand2,
            'operator':operator
        })
