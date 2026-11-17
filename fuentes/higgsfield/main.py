"""Ejemplo: genera un video con Seedance 2.5 (texto a video) en la API de Higgsfield.

Uso:  cd fuentes/higgsfield && .venv/bin/python main.py
La clave va en .env.local (HF_KEY=key-id:key-secret). Nunca se imprime ni se commitea.
Cada ejecución es una generación con costo.
"""
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

load_dotenv(Path(__file__).with_name(".env.local"))

import higgsfield_client  # noqa: E402  (se importa después de cargar HF_KEY)
from higgsfield_client.types_ import NSFW, Cancelled, Completed, Failed  # noqa: E402

MODELO = "bytedance/seedance-2.5/text-to-video"
ARGUMENTOS = {
    "prompt": "A cinematic scene at sunset",
    "duration": 5,
    "resolution": "720p",
    "aspect_ratio": "16:9",
}


def main() -> int:
    if not os.getenv("HF_KEY"):
        print("Falta HF_KEY en fuentes/higgsfield/.env.local (formato key-id:key-secret).")
        return 1

    estado_final = {}

    def al_encolar(request_id: str) -> None:
        print(f"Pedido enviado: {request_id}")

    def al_actualizar(estado) -> None:
        estado_final["valor"] = estado
        print(f"Estado: {type(estado).__name__}")

    try:
        resultado = higgsfield_client.subscribe(
            MODELO,
            arguments=ARGUMENTOS,
            on_enqueue=al_encolar,
            on_queue_update=al_actualizar,
        )
    except Exception as error:  # error de red, credenciales o validación
        print(f"La generación no se pudo completar: {type(error).__name__}: {error}")
        return 1

    estado = estado_final.get("valor")
    if isinstance(estado, NSFW):
        print("La generación fue bloqueada por moderación.")
        return 1
    if isinstance(estado, Cancelled):
        print("La generación fue cancelada.")
        return 1
    if isinstance(estado, Failed) or not isinstance(estado, Completed):
        print(f"La generación falló (estado: {resultado.get('status', 'desconocido')}).")
        return 1

    url = (resultado.get("video") or {}).get("url")
    if not url:
        print("La generación terminó pero no devolvió la URL del video.")
        return 1

    print(f"Video listo: {url}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
