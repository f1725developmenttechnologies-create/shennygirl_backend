```python
from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.security import APIKeyHeader
import os
from datetime import datetime
from app.utils.supabase_client import SupabaseClient

router = APIRouter()
api_key_header = APIKeyHeader(name="X-API-Key", auto_error=False)

# Función de autenticación
async def verify_api_key(request: Request, api_key: str = Depends(api_key_header)):
    if not api_key:
        raise HTTPException(status_code=401, detail="API Key requerida")
    expected_key = os.getenv("API_KEY")
    if api_key != expected_key:
        raise HTTPException(status_code=403, detail="API Key inválida")
    
    # Registrar auditoría (opcional, pero lo dejamos para trazabilidad)
    try:
        client = SupabaseClient.get_client()
        client.table("audit_logs").insert({
            "timestamp": datetime.now().isoformat(),
            "endpoint": str(request.url),
            "method": request.method,
            "ip": request.client.host if request.client else "unknown"
        }).execute()
    except Exception:
        pass  # No fallar si no se puede loggear
    return True

# Endpoint de prueba de seguridad (solo accesible con API Key)
@router.get("/test-auth")
async def test_auth(auth=Depends(verify_api_key)):
    return {"message": "Autenticación exitosa"}
```