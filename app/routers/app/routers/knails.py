from fastapi import APIRouter, File, UploadFile, Form, Depends
import cv2, numpy as np, base64
from app.routers.kshield import verify_api_key

router = APIRouter()

@router.post("/simulate/nails")
async def simulate_nails(file: UploadFile = File(...), pattern: str = Form(...), auth=Depends(verify_api_key)):
    # Placeholder: devuelve la imagen original con un filtro de color en las uñas (simulado)
    contents = await file.read()
    nparr = np.frombuffer(contents, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Simulación: aumentar el brillo en la zona de las manos (no real)
    h, w, _ = img.shape
    for i in range(h):
        for j in range(w):
            if i > h//2 and j > w//4 and j < 3*w//4:
                img[i,j] = (img[i,j] * 1.3).astype(np.uint8)
    
    _, buffer = cv2.imencode('.jpg', img)
    img_base64 = base64.b64encode(buffer).decode('utf-8')
    return {"image": img_base64}