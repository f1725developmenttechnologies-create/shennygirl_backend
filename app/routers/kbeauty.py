from fastapi import APIRouter, File, UploadFile, Form, Depends
from fastapi.responses import JSONResponse
import cv2
import numpy as np
import base64
from app.routers.kshield import verify_api_key

router = APIRouter()

@router.post("/analyze/skin")
async def analyze_skin(file: UploadFile = File(...), auth=Depends(verify_api_key)):
    # Lectura de la imagen (simulación)
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Simulación: calcular promedio de color en la zona central (simplificado)
    h, w, _ = img.shape
    crop = img[h//4:3*h//4, w//4:3*w//4]
    avg_color = cv2.mean(crop)[:3]  # (B, G, R)
    hex_color = f"#{int(avg_color[2]):02x}{int(avg_color[1]):02x}{int(avg_color[0]):02x}"
    
    return {
        "skin_tone_hex": hex_color,
        "recommendations": {
            "blush": ["rosa", "melocotón"],
            "lipstick": ["nude", "coral"],
            "hair_color": ["cobre", "miel"]
        }
    }

@router.post("/simulate/hair")
async def simulate_hair(file: UploadFile = File(...), color_hex: str = Form(...), auth=Depends(verify_api_key)):
    # Aquí iría la lógica con MediaPipe (por ahora devolvemos la misma imagen con un filtro básico)
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Convertir color_hex a BGR
    color = tuple(int(color_hex[i:i+2], 16) for i in (1, 3, 5))  # (R,G,B)
    # Aplicar un tinte ligero en toda la imagen (simulación)
    # En realidad aquí iría la segmentación de cabello y solo aplicar color ahí.
    h, w, _ = img.shape
    for i in range(h):
        for j in range(w):
            img[i,j] = (img[i,j] * 0.6 + np.array(color) * 0.4).astype(np.uint8)
    
    _, buffer = cv2.imencode('.jpg', img)
    img_base64 = base64.b64encode(buffer).decode('utf-8')
    return {"image": img_base64}

@router.post("/simulate/makeup")
async def simulate_makeup(file: UploadFile = File(...), auth=Depends(verify_api_key)):
    # Similar al anterior, pero para labios/ojos (simulación)
    # Por ahora devolvemos un mensaje
    return {"message": "Makeup simulation endpoint (placeholder)"}