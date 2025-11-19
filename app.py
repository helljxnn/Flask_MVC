# Importaciones necesarias
from flask import Flask, render_template, request
from models.triangulo import calcular_triangulo

# Inicialización de la aplicación Flask
app = Flask(__name__)

# Ruta principal que maneja el formulario y muestra resultados
@app.route('/', methods=['GET', 'POST'])
def formulario_triangulo():
    area = None
    perimetro = None

    if request.method == 'POST':
        try:
            base = float(request.form.get('base', 0))
            altura = float(request.form.get('altura', 0))
            lado1 = float(request.form.get('lado1', 0))
            lado2 = float(request.form.get('lado2', 0))
            area, perimetro = calcular_triangulo(base, altura, lado1, lado2)
        except ValueError:
            area = None
            perimetro = None

    return render_template('triangulo.html', area=area, perimetro=perimetro)


# Ejecución de la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True) #Se pone solo en desarrollo para que al hacer cambios se reinicie el servidor