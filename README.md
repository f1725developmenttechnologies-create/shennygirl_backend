# shennygirl_backend
academia de belleza
# SHENNYGIRL NAILS ACADEMY — Backend de IA y Negocio

**Arquitecto:** F1725  
**Propósito:** Servicio de API FastAPI para la gestión de clientes, citas, facturación, simulación de estilismo (AR) y generación de avatares 3D. Este backend es el cerebro del ecosistema ShennyGirl, diseñado para desplegarse en **Hugging Face Spaces** (GPU T4 gratuita) o en un servidor local con Ngrok.

---

## 🧬 Arquitectura

- **Framework:** FastAPI (Python 3.10)  
- **Base de Datos:** Supabase (PostgreSQL)  
- **Modelos de IA:** MediaPipe (Face Mesh, Hands, Selfie Segmentation), OpenCV, PyTorch, Trimesh  
- **Seguridad:** KSHIELD (autenticación por API-Key, watermarking DCT, auditoría en Supabase)  
- **Infraestructura:** HF Spaces (producción) / Ngrok (desarrollo/respaldo)

---

## 📁 Estructura del Proyecto
shennygirl-backend/
├── .github/workflows/
│   └── deploy-hf.yml
├── app/
│   ├── main.py
│   ├── routers/
│   │   ├── kshield.py
│   │   ├── kbeauty.py
│   │   ├── knails.py
│   │   ├── avatar3d.py
│   │   └── business.py   # (si no lo tienes, lo completo)
│   ├── models/
│   │   ├── hair_model.py
│   │   ├── face_model.py
│   │   ├── hand_model.py
│   │   └── avatar_model.py
│   ├── utils/
│   │   ├── watermark.py
│   │   ├── supabase_client.py
│   │   ├── image_ops.py
│   │   └── face_utils.py
│   └── __init__.py
├── requirements.txt
├── Dockerfile
└── .env.example
