import pandas as pd

def procesar_archivo_personalizado(file_path):

    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    else:

        df = pd.read_excel(file_path)


    df.columns = df.columns.str.strip().str.lower()


    if 'prioridad' not in df.columns:
        df['prioridad'] = 'Baja'
    else:

        df['prioridad'] = df['prioridad'].astype(str).str.strip().str.capitalize()


    try:
        df['fecha_entrega'] = pd.to_datetime(df['fecha_entrega']).dt.strftime('%Y-%m-%d')
    except Exception as e:
        print(f"Error en formato de fecha: {e}")

    df['estado'] = 'Pendiente'

    return df.to_dict(orient='records')