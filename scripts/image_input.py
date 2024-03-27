from imports import cv2, os, np, tf, ImageDataGenerator

def read_images_in_folder(folder_path):
    images = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(folder_path, filename)
            image = cv2.imread(image_path)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = cv2.resize(image, (250, 250))
            if image is not None:
                images.append(image)
    return images

folder_path = '../data/images/'
images = read_images_in_folder(folder_path)

def augment_images(images):
    train_datagen = ImageDataGenerator(rescale=1./255,
                                        rotation_range=40,
                                        width_shift_range=0.2,
                                        height_shift_range=0.2,
                                        shear_range=0.2,
                                        zoom_range=0.2,
                                        horizontal_flip=True,
                                        fill_mode='nearest')
    augmented_images = []
    for image in images:
        image = np.expand_dims(image, 0)
        i = 0
        for batch in train_datagen.flow(image, batch_size=1):
            augmented_images.append(batch)
            i += 1
            if i >= 50:
                break
    return augmented_images

augmented_images = augment_images(images)
augment_images = np.array(augmented_images).reshape(-1, 250, 250, 3)

