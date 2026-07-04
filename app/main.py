import os
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

# Importar los routers (aunque aún no los hayas creado, las importaciones quedarán listas)
from app.routers import business, kshield, kbeauty, knails, avatar3d

# Inicializar la app
app = FastAPI(
    title="ShennyGirl Nails Academy API",
    description="Backend para gestión de negocio, IA y seguridad del ecosistema F1725-Ω",
    version="1.0.0"
)

# Configurar CORS (permite que la app móvil y la PWA se conecten)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # En producción, restringir a tu dominio de Vercel/Netlify
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Middleware de autenticación global (KSHIELD) - lo implementaremos después
# Por ahora, solo importamos el router de seguridad

# Incluir los routers
app.include_router(business.router, prefix="/api/business", tags=["Negocio"])
app.include_router(kshield.router, prefix="/api/kshield", tags=["Seguridad"])
app.include_router(kbeauty.router, prefix="/api/kbeauty", tags=["Estética"])
app.include_router(knails.router, prefix="/api/knails", tags=["Uñas"])
app.include_router(avatar3d.router, prefix="/api/avatar", tags=["3D"])

# Endpoint de prueba (health check)
@app.get("/health")
async def health_check():
    return {"status": "ok", "message": "ShennyGirl backend is alive"}

# Endpoint raíz
@app.get("/")
async def root():
    return {
        "project": "ShennyGirl Nails Academy",
        "version": "1.0.0",
        "docs": "/docs",
        "status": "operational"
    }

# Si ejecutas directamente este archivo (para pruebas locales)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)