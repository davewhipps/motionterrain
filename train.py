from tflite_model_maker import image_classifier
from tflite_model_maker.image_classifier import DataLoader

# Load input data specific to an on-device ML app.
train_data = DataLoader.from_folder('../lavated_data_split/train')
validation_data = DataLoader.from_folder('../lavated_data_split/val')
test_data = DataLoader.from_folder('../lavated_data_split/test')

# Customize the TensorFlow model.
model = image_classifier.create(train_data,
                            	validation_data=validation_data,
								model_spec='mobilenet_v2',
								batch_size=32,
								epochs=50,
								train_whole_model=True,
								dropout_rate=0.5,
								learning_rate=0.0001,
								shuffle=True,
								use_augmentation=True)

# Evaluate the model.
loss, accuracy = model.evaluate(test_data)

# Export to Tensorflow Lite model and label file in `export_dir`.
model.export(export_dir='./',
             tflite_filename='motionterrain_simple.tflite')