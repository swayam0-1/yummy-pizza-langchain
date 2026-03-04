import qrcode
from PIL import Image
import io

def generate_upi_qr(amount: float, upi_id: str = "demo@swayam", name: str = "Pizza Bot") -> Image.Image:
    """Generate a UPI payment QR code image."""
    upi_string = f"upi://pay?pa={upi_id}&pn={name}&am={amount}&cu=INR&tn=PizzaOrder"

    qr = qrcode.QRCode(
        version=2,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=8,
        border=4,
    )
    qr.add_data(upi_string)
    qr.make(fit=True)

    img = qr.make_image(fill_color="#1a1a2e", back_color="white")
    return img

def qr_to_bytes(img: Image.Image) -> bytes:
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()
