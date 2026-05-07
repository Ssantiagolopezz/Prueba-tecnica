from fastapi import FastAPI, UploadFile, File, Depends
from sqlalchemy.orm import Session
import shutil
import os
from database import SessionLocal, init_db, Orden
from logic import procesar_archivo_personalizado

app = FastAPI()

from fastapi.middleware.cors import CORSMiddleware



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


init_db()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(file.file.read())

    
    from logic import procesar_archivo_personalizado
    datos_procesados = procesar_archivo_personalizado(file_location)

   
    for item in datos_procesados:
        nueva_orden = Orden(
            proveedor=item['proveedor'],
            producto=item['producto'],
            cantidad=item['cantidad'],
            fecha_entrega=item['fecha_entrega'],
            prioridad=item['prioridad'], 
            estado=item['estado']
        )
        db.add(nueva_orden)
    
    db.commit()
    return {"message": "Archivo procesado con prioridades manuales"}

@app.get("/ordenes")
def listar_ordenes(prioridad: str = None, proveedor: str = None, db: Session = Depends(get_db)):
    query = db.query(Orden)
    if prioridad:
        query = query.filter(Orden.prioridad == prioridad)
    if proveedor:
        query = query.filter(Orden.proveedor == proveedor)
    return query.all()

@app.delete("/ordenes/vaciar")
def vaciar_ordenes(db: Session = Depends(get_db)):
    try:
        
        num_borrados = db.query(Orden).delete()
        db.commit()
        return {"message": f"Se eliminaron {num_borrados} órdenes correctamente"}
    except Exception as e:
        db.rollback()
        return {"error": str(e)}

@app.put("/ordenes/{orden_id}/estado")
def actualizar_estado(orden_id: int, nuevo_estado: str, db: Session = Depends(get_db)):
    orden = db.query(Orden).filter(Orden.id == orden_id).first()
    if not orden:
        return {"error": "Orden no encontrada"}
    
    orden.estado = nuevo_estado
    db.commit()
    return {"message": "Estado actualizado", "nuevo_estado": nuevo_estado}