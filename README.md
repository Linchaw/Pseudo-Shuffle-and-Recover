# Pseudo-Shuffle-and-Recover （有中文介绍）
Pseudo shuffle for bytes, array(numpy),  image(open by opencv) and Recover <br>
requirement ： pip install numpy opencv

# 中文版：
对字符串数据，以及numpy的数组数据（包括图像）进行随机置乱
并且可以通过相同的随机数种子对置乱的图像恢复
## 对字节数据置乱的例子 
原始字节数据：<br>
`bytes = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x02\x00\x00\x00\x02\x00\x08\x02\x00\x00\x00{\x1aC'`<br>

置乱代码：<br>
`shuffle_data = bytes_shuffle(data, seed=1)`<br>

置乱后的字节数据：<br>
`shuffle_data = b'\x00G\x02\x02\x00\x00\x00\x00\x00D\x08\x00\x00\x00\rN\x02\x1aH\n{P\x00\x89RC\x1a\x00\x00I\r\n'`<br>

恢复代码：<br>
`recover_data = bytes_sort(shuffle_data, seed=1)`<br>

恢复后的字节数据：<br>
`recover_data = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x02\x00\x00\x00\x02\x00\x08\x02\x00\x00\x00{\x1aC'`<br>

## 对图像数据置乱的例子
原始图像：<br>
![lena](https://user-images.githubusercontent.com/110237013/195288871-7bebc8c8-258b-4bd8-bc31-f41a52fae616.png)

置乱后的图像：<br>
![shuffle_lena](https://user-images.githubusercontent.com/110237013/195288964-8a463f0e-895c-4fa8-a790-90c2e3055e35.png)

恢复图像：<br>
![recover_lena](https://user-images.githubusercontent.com/110237013/195289058-c08162c6-5305-4276-aca6-747a2c6fbcca.png)

