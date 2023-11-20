from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def inicio():

    if request.method == 'POST':
        valor = request.form['valor']
        if valor == "1":
            return redirect(url_for('ejercicio1'))

        if valor == "2":
            return redirect(url_for('ejercicio2'))

    return render_template("index.html")


@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])
        promedio = (nota1 + nota2 + nota3) / 3
        if promedio >= 40 and asistencia >= 75:
            aprobado = "APROBADO"
        else:
            aprobado = "REPROBADO"
        return render_template("ejercicio1.html", promedio=promedio, aprobado=aprobado)

    return render_template("ejercicio1.html")


@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']
        largo1 = len(nombre1)
        largo2 = len(nombre2)
        largo3 = len(nombre3)

        mayor = max(largo1, largo2, largo3)
        nombre = max(nombre1, nombre2, nombre3, key=len)
        return render_template("ejercicio2.html", mayor=mayor, nombre=nombre)

    return render_template("ejercicio2.html")


if __name__ == '__main__':
    app.run(debug=True)
