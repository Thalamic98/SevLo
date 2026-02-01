import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer

# 1. PON AQUÍ TU ENLACE REAL
# Ve a tu navegador, copia el link de tu página y pégalo aquí entre comillas:
url_sevlo = "https://sevloth.github.io/sevlo/" 

print(f"Generando QR para: {url_sevlo}")

# 2. Configuración para Alta Resolución (para impresión)
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H, # H = High (Resiste manchas o arrugas)
    box_size=50, # 50 pixeles por cuadro (Saldrá una imagen GRANDE y nítida)
    border=2,
)

qr.add_data(url_sevlo)
qr.make(fit=True)

# 3. Personalización Estilo Sevlo
# Usamos negro o gris muy oscuro para que contraste bien y los teléfonos lo lean rápido.
img = qr.make_image(
    fill_color="#2D2D2D", # El gris oscuro elegante de tu página
    back_color="white",
    module_drawer=RoundedModuleDrawer() # Esto hace que los puntitos sean REDONDOS (más moderno)
)

# 4. Guardar
nombre_archivo = "QR_Sevlo_Oficial.png"
img.save(nombre_archivo)

print(f"¡Listo! Revisa tu carpeta, ahí está la imagen: {nombre_archivo}")