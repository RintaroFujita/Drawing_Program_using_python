from google.colab import drive
drive.mount('/content/drive')

import matplotlib.pyplot as plt
import numpy as np
import os
import uuid

save_directory = '/content/drive/MyDrive/I2T Recognition Dataset/Line'  # 必要に応じてパスを変更
os.makedirs(save_directory, exist_ok=True)

def generate_and_save_image():

    plt.figure(figsize=(4, 4))

    points = np.random.rand(10, 2) * 400

    for i in range(len(points) - 1):
        p1 = points[i]
        p2 = points[i + 1]


        cp1 = p1 + np.random.rand(2) * 100 - 50
        cp2 = p2 + np.random.rand(2) * 100 - 50


        t = np.linspace(0, 1, 100)
        curve_x = (1 - t)**3 * p1[0] + \
                   3 * (1 - t)**2 * t * cp1[0] + \
                   3 * (1 - t) * t**2 * cp2[0] + \
                   t**3 * p2[0]

        curve_y = (1 - t)**3 * p1[1] + \
                   3 * (1 - t)**2 * t * cp1[1] + \
                   3 * (1 - t) * t**2 * cp2[1] + \
                   t**3 * p2[1]

        plt.plot(curve_x, curve_y, color='black', lw=5)

    unique_id = uuid.uuid4()
    file_name = f'image_{unique_id}.jpg'
    plt.axis('off')
    plt.savefig(os.path.join(save_directory, file_name), bbox_inches='tight', pad_inches=0)
    plt.close()

for _ in range(9300):
    generate_and_save_image()