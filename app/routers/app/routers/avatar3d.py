from fastapi import APIRouter, File, UploadFile, Depends, Response
import io
import trimesh
import numpy as np
from app.routers.kshield import verify_api_key

router = APIRouter()

@router.post("/generate/avatar")
async def generate_avatar(file: UploadFile = File(...), auth=Depends(verify_api_key)):
    # Simulación de generación de malla: crea una esfera (placeholder) y la devuelve como .glb
    # En producción, aquí usarías un modelo como DECA.
    mesh = trimesh.primitives.Sphere(radius=1.0)
    # Añadir algunos puntos para simular una cabeza (solo para demostrar)
    # Realmente aquí cargarías un modelo preentrenado.
    
    # Exportar a GLB
    glb_data = mesh.export(file_type='glb')
    return Response(content=glb_data, media_type="application/octet-stream", headers={"Content-Disposition": "attachment; filename=avatar.glb"})