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

