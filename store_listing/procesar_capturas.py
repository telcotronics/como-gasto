import os
import subprocess
import time
from PIL import Image

ADB_PATH = "/home/pablinux/Android/Sdk/platform-tools/adb"
OUTPUT_DIR = "store_listing/graficos"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Coordenadas matemáticas para recorte simétrico de barras de sistema en resolución 1344x2992 (Pixel 8 Pro):
# (0, 152, 1344, 152 + 2688) -> Elimina barra de estado superior (152px) y barra de gestos inferior (152px)
# Genera una imagen exacta de 1344 x 2688 (Relación 1:2 / 2:1), formato oficial para Google Play / App Store.
CROP_BOX = (0, 152, 1344, 152 + 2688)

def capturar_pantalla(nombre_archivo):
    raw_path = f"/tmp/{nombre_archivo}_raw.png"
    dest_path = os.path.join(OUTPUT_DIR, f"{nombre_archivo}.png")
    
    # 1. Tomar screenshot limpio desde ADB
    cmd = f"{ADB_PATH} exec-out screencap -p > {raw_path}"
    subprocess.run(cmd, shell=True, check=True)
    
    # 2. Recortar simétricamente con PIL
    im = Image.open(raw_path)
    if im.size == (1344, 2992):
        im_cropped = im.crop(CROP_BOX)
    else:
        # Si la resolución difiere, calcular recorte simétrico proporcional 2:1
        w, h = im.size
        target_h = int(w * 2)
        margin = (h - target_h) // 2
        im_cropped = im.crop((0, margin, w, margin + target_h))
        
    im_cropped.save(dest_path, "PNG", optimize=True)
    print(f"✓ Captura guardada: {dest_path} -> Tamaño: {im_cropped.size} (Relación 1:2 / 2:1)")
    return dest_path

def tap(x, y, delay=1.5):
    subprocess.run(f"{ADB_PATH} shell input tap {x} {y}", shell=True)
    time.sleep(delay)

def swipe(x1, y1, x2, y2, duration=300, delay=1.5):
    subprocess.run(f"{ADB_PATH} shell input swipe {x1} {y1} {x2} {y2} {duration}", shell=True)
    time.sleep(delay)

def key(keycode, delay=1.0):
    subprocess.run(f"{ADB_PATH} shell input keyevent {keycode}", shell=True)
    time.sleep(delay)

if __name__ == "__main__":
    print("Script de captura y recorte simétrico ADB preparado.")
    # Verificar conexión con dispositivo ADB
    res = subprocess.run(f"{ADB_PATH} devices", shell=True, capture_output=True, text=True)
    print("Dispositivos detectados:")
    print(res.stdout)
