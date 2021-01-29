# coding=utf-8
# 引入必须的库文件
from PIL import Image,ImageDraw,ImageFont

def make_text(info,filename):
    # 获取文字信息
    uptext = info[0]
    downtext = info[1]
    # 设置字体，这里选择了更纱黑体，斜体，70号字
    font = ImageFont.truetype("sarasa-bolditalic.ttc", 70)
    # 新建一个背景文件，把Draw对象初始化
    background = Image.new(mode = 'RGBA',size = (500,500),color = 'white')
    draw = ImageDraw.Draw(background)
    # 通过textSize函数获取文字所占面积
    up_size_width,up_size_heigth = draw.textsize(uptext, font=font, spacing=6)
    down_size_width,down_size_heigth = draw.textsize(downtext, font=font, spacing=6)
    # 通过文字面积计算图片面积
    image_size = (down_size_width+130,down_size_heigth+up_size_heigth+30)
    # 修改背景文件大小并为背景赋值渐变色
    background = background.resize(image_size, Image.ANTIALIAS)
    color_list_one = [[255,255,255],[209,100,35],[138,3,0],[196,19,25],[12,4,2],[242,242,242],[162,181,188],[242,242,242],[255,255,255]]
    color_size_one = [10,40,10,25,10,42,42,10]
    background = make_change_color(background,color_list_one,color_size_one)
    # 配置描边渐变图层，设置描边渐变色
    contur_color_layer = Image.new(mode = 'RGBA',size = image_size,color = 'white')
    color_list_two = [[0,0,0],[64,53,54],[192,193,194],[49,60,60],[162,168,157],[127,113,116],[220,210,210],[0,0,0],[64,53,54],[192,193,194],[49,60,60],[162,168,157],[127,113,116],[220,210,210]]
    color_size_two = [10,15,20,25,25,17,10,10,15,20,25,25,17]
    draw = ImageDraw.Draw(contur_color_layer)
    make_change_color(contur_color_layer,color_list_two,color_size_two)
    # 配置文字图层，绘画透明的文字外边框
    middle_layer = Image.new(mode = 'RGBA',size = image_size,color = 'white')
    draw = ImageDraw.Draw(middle_layer)
    make_text_contur(draw,(11,11), uptext,font,(203,181,107,0),(219,209,216,0),5)
    make_text_contur(draw,(111,up_size_heigth+11), downtext,font,(203,181,107,0),(219,209,216,0),5)
    # 将透明的文字图层和渐变图层合并，文字图层在上，渐变图层在下
    middle_layer = Image.alpha_composite(contur_color_layer,middle_layer)
    # 绘画描边
    draw = ImageDraw.Draw(middle_layer)
    make_text_contur(draw,(9,11), uptext,font,(238,198,15,255),(238,198,15,255),3)
    make_text_contur(draw,(109,up_size_heigth+11), downtext,font,(71,73,85,255),(0,0,0,255),3)
    make_text_contur(draw,(109,up_size_heigth+11), downtext,font,(71,73,85,255),(71,73,85,255),1)
    # 将主要文字扣成透明色，准备和背景图层合并
    draw.text((10,10), uptext, fill=(0,0,0,0), font=font)
    draw.text((110,up_size_heigth+10), downtext, fill=(0,0,0,0), font=font)
    # 文字图层和背景图层合并，文字图层在上，背景图层在下
    background = Image.alpha_composite(background, middle_layer)
    background.save(filename)

def make_text_contur(draw, pos, text, font, fill, border='black', abp=1):
    # 将文字向周边移动后描绘实现描边效果
    x, y = pos
    shadowcolor = border
    for bp in range(1,abp):
        draw.text((x-bp, y), text, font=font, fill=shadowcolor)
        draw.text((x+bp, y), text, font=font, fill=shadowcolor)
        draw.text((x, y-bp), text, font=font, fill=shadowcolor)
        draw.text((x, y+bp), text, font=font, fill=shadowcolor)
        draw.text((x-bp, y-bp), text, font=font, fill=shadowcolor)
        draw.text((x+bp, y-bp), text, font=font, fill=shadowcolor)
        draw.text((x-bp, y+bp), text, font=font, fill=shadowcolor)
        draw.text((x+bp, y+bp), text, font=font, fill=shadowcolor)
    draw.text((x, y), text, font=font, fill=fill)

def make_change_color(image,color_list,color_size):
    # 对颜色进行演算并逐行填充到图片上实现渐变效果。
    image_size = image.size
    draw = ImageDraw.Draw(image)
    color_change_start = 0
    for color_flag in range(0,len(color_size)):
        color_start = color_list[color_flag]
        color_end = color_list[color_flag+1]
        color_length = color_size[color_flag]
        # 这里简化了运算，因为简化运算在部分情况下会造成图片发生颜色条纹
        color_step_R = int((color_start[0]-color_end[0])/color_length)
        color_step_G = int((color_start[1]-color_end[1])/color_length)
        color_step_B = int((color_start[2]-color_end[2])/color_length)
        for y in range(color_change_start,color_change_start+color_length):
            # 将步进参数赋值到颜色上
            color_fill_R = color_start[0] - color_step_R * (y-color_change_start)
            color_fill_G = color_start[1] - color_step_G * (y-color_change_start)
            color_fill_B = color_start[2] - color_step_B * (y-color_change_start)
            for x in range(0,image_size[0]):
                draw.point((x,y),fill = (color_fill_R,color_fill_G,color_fill_B))
        color_change_start = color_change_start + color_length;
    return image

if __name__ == "__main__":
    # execute only if run as a script
    make_text(['用Python生成','大鸟转转酒吧！'],'test.png')