import qrcode
from PIL import Image

q = qrcode.QRCode(version=1 ,error_correction=qrcode.ERROR_CORRECT_H ,
                 box_size=10 , border=4)

q.add_data("https://github.com/amanavaa")
q.make(fit=True)

finalqr = q.make_image(fill_color="green" , back_color="white")
finalqr.save("mygithub.png")