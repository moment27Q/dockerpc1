# TikTok Downloader (Flask + yt-dlp)

App web simple para descargar un video a partir de una URL. La interfaz se muestra en el navegador y el archivo se guarda en la carpeta `videos/`.

## Requisitos
- Python 3.11+ (recomendado)
- `pip`
- (Opcional) `ffmpeg` instalado en el sistema para mejores resultados de descarga y conversión

## Ejecucion local (Windows / PowerShell)
```powershell
cd C:\Users\matia\OneDrive\Escritorio\pc1\tiktok-downloader
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app.py
```

Abrir en el navegador:
```
http://localhost:5000
```

Los videos descargados se guardan en:
```
videos/
```

## Ejecucion con Docker

### Imagen base (v1)
```powershell
docker build -t tiktok:v1 -f Dockerfile .
docker run --rm -p 5000:5000 -v ${PWD}\videos:/app/videos tiktok:v1
```

### Imagen optimizada (v2)
```powershell
docker build -t tiktok:v2 -f Dockerfile.optimizado .
docker run --rm -p 5000:5000 -v ${PWD}\videos:/app/videos tiktok:v2
```

### Imagen multistage (v3)
```powershell
docker build -t tiktok:v3 -f Dockerfile.multistage .
docker run --rm -p 5000:5000 -v ${PWD}\videos:/app/videos tiktok:v3
```

Abrir en el navegador:
```
http://localhost:5000
```

## Notas
- Si usas Docker, la carpeta `videos/` se monta como volumen para conservar las descargas en tu equipo.
- Si algo falla al descargar, revisa la consola donde corre la app para ver el error exacto.
