import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Cargar datos desde archivos locales
volumen = pd.read_csv("mercado_muebles_canada/volumen_exportado.csv")
distribuidores = pd.read_csv("mercado_muebles_canada/nuevos_distribuidores.csv")
online = pd.read_csv("mercado_muebles_canada/cantidad_compra_online.csv")
genero = pd.read_csv("mercado_muebles_canada/tendencia_genero.csv")
edad = pd.read_csv("mercado_muebles_canada/rango_edad.csv")
sostenibilidad = pd.read_csv("mercado_muebles_canada/importancia_sostenibilidad.csv")

# Inicializar la aplicación Dash
app = dash.Dash(__name__)
app.title = "Dashboard Mercado de Muebles en Canadá"

# Diseño del dashboard
app.layout = html.Div([
    html.H1("Dashboard Mercado de Muebles en Canadá", style={"textAlign": "center"}),

    dcc.Graph(
        figure=px.line(volumen, x="Año", y="Volumen Exportado (millones CAD)",
                       title="Volumen Exportado de Muebles")
    ),

    dcc.Graph(
        figure=px.bar(distribuidores, x="Año", y="Nuevos Distribuidores",
                      title="Nuevos Distribuidores por Año")
    ),

    dcc.Graph(
        figure=px.line(online, x="Año", y="Porcentaje Compras en Línea (%)",
                       title="Crecimiento de Compras en Línea")
    ),

    dcc.Graph(
        figure=px.pie(genero, names="Género", values="Porcentaje de Compras (%)",
                      title="Distribución de Compras por Género")
    ),

    dcc.Graph(
        figure=px.bar(edad, x="Rango de Edad", y="Porcentaje de Compras (%)",
                      title="Compras por Rango de Edad")
    ),

    dcc.Graph(
        figure=px.line(sostenibilidad, x="Año", y="Clientes que Valoran la Sostenibilidad (%)",
                       title="Importancia de la Sostenibilidad para los Clientes")
    ),
])

# Ejecutar el servidor
if __name__ == "__main__":
    app.run_server(debug=True)
