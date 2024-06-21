from PIL import Image,ImageDraw,ImageFont
import os

def add_watermark_overlay(input_image_path, output_image_path, watermark_text):
    input_image=Image.open(input_image_path)
    input_image=input_image.convert('RGBA')
    width,height=input_image.size

    overlay=Image.new('RGBA',input_image.size,(255,255,255,0))

    draw=ImageDraw.Draw(overlay)

    watermark_color_pattern=(255,255,255,30)

    for i in range(0,width+height,50):
        draw.line([(0,height-i),(i,height)], fill=watermark_color_pattern, width=5)
    
    font_size=80
    try:
        font=ImageFont.truetype('arial.ttf',font_size)
    except IOError:
        font=ImageFont.load_default()
    text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width, text_height = text_bbox[2] - text_bbox[0], text_bbox[3] - text_bbox[1]

    x=(width-text_width)//2
    y=(height-text_height)//2

    watermark_color_text=(255,255,255,80)

    draw.text((x,y),watermark_text,fill=watermark_color_text,font=font)

    watermarked_image=Image.alpha_composite(input_image,overlay)

    if output_image_path.lower().endswith('.jpg') or output_image_path.lower().endswith('.jpeg'):
    
        rgb_watermarked_image = watermarked_image.convert('RGB')
        rgb_watermarked_image.save(output_image_path, 'JPEG')
    else:
        
        watermarked_image.save(output_image_path)

input_image_path = 'input_image.jpg'
output_image_directory = '/Users/vanshikajain/Desktop/project/output_images'
output_image_name = 'output_image.png' 
output_image_path = os.path.join(output_image_directory, output_image_name)
watermark_text = 'Vanshika Jain'

if not os.path.exists(output_image_directory):
    os.makedirs(output_image_directory)

add_watermark_overlay(input_image_path, output_image_path, watermark_text)
print(f'Watermark added successfully to {output_image_path}')