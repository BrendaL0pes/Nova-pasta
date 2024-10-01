import os
import io
import numpy as np
import matplotlib.pyplot as plt
from flask import Flask, render_template, request, send_file
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from mpl_toolkits.mplot3d import Axes3D  # Necessário para gráficos 3D

app = Flask(__name__)

# Rota principal para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

# Rota para gerar o gráfico com base nos parâmetros fornecidos
@app.route('/plot', methods=['POST'])
def plot_graph():
    lambda_ = float(request.form['lambda_'])
    beta = float(request.form['beta'])
    plot_type = request.form['plot_type']
    
    # Geração dos dados de x e y
    x_vals = np.linspace(-10, 10, 400)
    y_vals = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x_vals, y_vals)

    # Função de interferência
    def calculate_interference(lambda_, beta, x, y):
        beta_rad = np.radians(beta)
        term1 = -2 * np.pi / lambda_
        eq_lambda = term1 * (np.cos(beta_rad) * x - np.sin(beta_rad) * y)
        eq_geral = 2 + 2 * np.cos(eq_lambda)
        return eq_geral

    Z = calculate_interference(lambda_, beta, X, Y)

    # Gerar o gráfico
    fig = plt.figure(figsize=(10, 7))

    # Verifica se o gráfico é 2D ou 3D com base na seleção do usuário
    if plot_type == '2d':
        ax = fig.add_subplot(111)
        contour = ax.contourf(X, Y, Z, levels=100, cmap='viridis')
        plt.colorbar(contour)
    elif plot_type == '3d':
        ax = fig.add_subplot(111, projection='3d')
        ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_zlabel('Interferência')

    # Salvar o gráfico como imagem
    img = io.BytesIO()  # Salva o gráfico na memória como bytes
    FigureCanvas(fig).print_png(img)
    img.seek(0)  # Reposiciona o cursor no início do arquivo

    # Retornar a imagem gerada como resposta
    return send_file(img, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
