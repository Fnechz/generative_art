from PIL import Image

im1 = Image.open(<path to image>)
im2 = Image.open(<path to image)
fg_resized = im2.resize((203, 248))  # 203 × 248 resize if images are not equal
blended = Image.blend(fg_resized,im1, alpha=0.5)
blended.save("blended1.png")
