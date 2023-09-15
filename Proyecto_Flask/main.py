from flask import Flask, render_template

app = Flask(__name__)

@app.route('/mapa/<path:lat>/<path:long>/<int:zoom>/<int:height>/<string:weight>/<string:cadena>')
def mapa1(lat, long, zoom, height, weight, cadena):
    return render_template('mapa2.html', lat=lat, long=long, zoom=zoom, height = height, weight = weight, cadena=cadena)

if __name__ == '__main__':
    app.run()


# from flask import Flask, render_template, url_for

# app = Flask(__name__)

# @app.route('/')
# def index():
#     edad = 18
#     #return "<h1>Bienvenidos a flask</h1>"
#     return render_template("index.html", dato2 = ["1", "2","3"])

# @app.route('/contacto')
# def contacto():
#     total = 100
#     #return "<h1>acto acto pide contacto</h1>"

# @app.route('/proyectos')
# @app.route('/proyectos/<string:nombre>/<int:edad>')
# def proyectos(nombre = None, edad = None):
#     if nombre is None:
#         return render_template("proyectos.html")
#     else:
#         return render_template("proyectos.html", nombre = nombre, edad = edad)

# @app.route('/loops')
# def loops():
#     lista = ["Frutas", "Verduras", "Limpieza", "Abarrotes"]
#     return render_template('loops.html',lista = lista)

# @app.route('/mapa/<float:lat>/<float:long>/<string:cadena>/<int:zoom>/<int:sizemap>')
# def mapa1(lat, long, cadena, zoom, sizemap):
#     return render_template('mapa2.html', lat=lat, long=long, cadena=cadena, zoom=zoom, sizemap=f"{sizemap}px")

# # @app.route('/mapa/<path:lat>/<path:long>/<string:cadena>')
# # def mapa(lat, long, cadena):
# #     return render_template('mapa.html', lat = lat, long = long, cadena = cadena)
