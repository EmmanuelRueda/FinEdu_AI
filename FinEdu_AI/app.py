from flask import Flask, render_template, request

app = Flask(__name__)

# Ahorro Simple
def calcular_ahorro_simple(capital, tasa, tiempo):
    return capital * (1 + tasa * tiempo)

# Ahorro Compuesto
def calcular_ahorro_compuesto(capital, tasa, tiempo):
    return capital * (1 + tasa)**tiempo

# Cuota de Préstamo
def calcular_cuota_prestamo(monto, tasa, plazo):
    tasa = tasa / 100 / 12
    plazo = plazo * 12
    return monto * tasa / (1 - (1 + tasa)**-plazo)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    tipo = request.form['tipo']
    capital = float(request.form['capital'])
    tasa = float(request.form['tasa']) / 100
    tiempo = int(request.form['tiempo'])

    if tipo == 'ahorro_simple':
        resultado = calcular_ahorro_simple(capital, tasa, tiempo)
    elif tipo == 'ahorro_compuesto':
        resultado = calcular_ahorro_compuesto(capital, tasa, tiempo)
    elif tipo == 'prestamo':
        resultado = calcular_cuota_prestamo(capital, tasa * 100, tiempo)
    else:
        resultado = 'Error'

    return render_template('index.html', resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

