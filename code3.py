# Pseudo-code to illustrate the process (not executable)

# Image Preprocessing (using VGG as an example)
image_model = VGG16(weights='imagenet')
image_model.layers.pop()  # Remove the classification layer
image_model = Model(inputs=image_model.inputs, outputs=image_model.layers[-1].output)

# Text Preprocessing (tokenization, creating vocabulary, etc.)

# Define the Encoder (CNN)
encoded_image = Input(shape=(image_feature_size,))
image_model_output = image_model(encoded_image)

# Define the Decoder (RNN)
decoder_input = Input(shape=(max_caption_length,))
decoder_output = some_RNN_layer()(decoder_input)

# Combine Encoder and Decoder
final_output = some_final_output_layer()(decoder_output)
model = Model(inputs=[encoded_image, decoder_input], outputs=final_output)

# Compile and Train the Model using image-caption pairs

# Generate captions for new images (inference)
