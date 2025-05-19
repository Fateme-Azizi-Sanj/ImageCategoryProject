import os
import random
import cv2
import matplotlib.pyplot as plt

# مسیر نسبی به پوشه sample_images
base_path = os.path.abspath("sample_images")

# بررسی وجود مسیر
if not os.path.exists(base_path):
    print("پوشه sample_images پیدا نشد.")
    exit()

# یافتن پوشه‌های دسته‌بندی
categories = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]

if not categories:
    print("هیچ دسته‌بندی‌ای پیدا نشد.")
    exit()

# از هر دسته‌بندی، یک تصویر تصادفی نمایش بده
for category in categories:
    category_path = os.path.join(base_path, category)
    image_files = [f for f in os.listdir(category_path) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]

    if not image_files:
        print(f"پوشه {category} خالی است.")
        continue

    selected_image = random.choice(image_files)
    image_path = os.path.join(category_path, selected_image)

    image = cv2.imread(image_path)

    if image is None:
        print(f"تصویر {selected_image} بارگذاری نشد.")
        continue

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image_blur = cv2.GaussianBlur(image_rgb, (9, 9), 0)

    # نمایش سه تصویر کنار هم
    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.imshow(image_rgb)
    plt.title('Original')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow(image_gray, cmap='gray')
    plt.title('Grayscale')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow(image_blur)
    plt.title('Blurred')
    plt.axis('off')

    plt.suptitle(f"{category} - {selected_image}", fontsize=14)
    plt.tight_layout()
    plt.show()
