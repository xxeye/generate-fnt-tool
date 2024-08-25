import tkinter as tk
from tkinter import filedialog, simpledialog, messagebox
from PIL import Image
import os

def generate_fnt_and_png(input_folder, output_folder, scale_size):
    base_name = os.path.basename(input_folder)
    output_fnt_path = os.path.join(output_folder, f"{base_name}.fnt")
    output_png_path = os.path.join(output_folder, f"{base_name}.png")
    
    # Load all images from the input folder
    images = []
    max_image_height = 0
    for file in sorted(os.listdir(input_folder)):
        if file.endswith(".png"):
            img_path = os.path.join(input_folder, file)
            img = Image.open(img_path)
            images.append((int(file.split('.')[0]), img))  # Store tuple of (id, image)
            max_image_height = max(max_image_height, img.height)

    # Sort images by ID
    images.sort(key=lambda x: x[0])

    # Create a single combined image (sprite sheet) with specified dimensions
    combined_image = Image.new('RGBA', (scale_size, scale_size))
    
    # Calculate positioning for images
    x_offset = 0
    y_offset = 0
    max_row_height = 0
    char_info = []
    for id, img in images:
        if x_offset + img.width > scale_size:  # Check if new row is needed
            x_offset = 0  # Reset x offset for new row
            y_offset += max_row_height  # Move down by the max height of the previous row
            max_row_height = 0  # Reset max row height

        if y_offset + img.height > scale_size:  # If adding another row exceeds the scale_size, break out
            break
        
        combined_image.paste(img, (x_offset, y_offset))  # Paste image at current position
        char_info.append({
            'id': id,
            'x': x_offset,
            'y': y_offset,
            'width': img.width,
            'height': img.height,
            'xoffset': 0,
            'yoffset': 0,
            'xadvance': img.width,
            'page': 0
        })
        x_offset += img.width
        max_row_height = max(max_row_height, img.height)

    # Save the combined image
    combined_image.save(output_png_path)

    # Write .fnt file
    with open(output_fnt_path, 'w') as f:
        f.write(f"info face=\"{base_name}\" size={max_image_height} bold=0 italic=0 charset=\"\" unicode=0 stretchH=100 smooth=1 aa=1 padding=0,0,0,0 spacing=1,1\n")
        f.write(f"common lineHeight={int(1.2 * max_image_height)} base={max_image_height} scaleW={scale_size} scaleH={scale_size} pages=1 packed=0\n")
        f.write("page id=0 file=\"" + os.path.basename(output_png_path) + "\"\n")
        f.write("chars count=" + str(len(char_info)) + "\n")
        for char in char_info:
            f.write(f"char id={char['id']} x={char['x']} y={char['y']} width={char['width']} height={char['height']} "
                    f"xoffset={char['xoffset']} yoffset={char['yoffset']} xadvance={char['xadvance']} page=0 chnl=0\n")
    
    # Display completion message
    messagebox.showinfo("完成", "輸出完畢！")
    sys.exit()

def main():
    root = tk.Tk()
    root.withdraw()  # 不显示主窗口

    # 用文件选择器获取输入文件夹路径
    input_folder = filedialog.askdirectory(title="選擇來源圖片資料夾")
    if not input_folder:
        return  # 用户取消操作

    # 用文件选择器获取输出文件夹路径
    output_folder = filedialog.askdirectory(title="選擇輸出資料夾")
    if not output_folder:
        return  # 用户取消操作

    # 用输入框获取纹理页面的大小
    scale_size = simpledialog.askinteger("輸入", "輸入纹理尺寸（預設方形）：", minvalue=1, maxvalue=10000)
    if scale_size is None:
               return  # 用户取消操作

    # 调用函数处理图片
    generate_fnt_and_png(input_folder, output_folder, scale_size)

    # 等待消息框关闭
    root.mainloop()

if __name__ == "__main__":
    main()
