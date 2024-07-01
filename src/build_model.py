def build_and_train_model(train_generator, validation_generator):
    # Build the CNN model
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(150, 150, 3)),
        MaxPooling2D((2, 2)),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Conv2D(128, (3, 3), activation='relu'),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(512, activation='relu'),
        Dropout(0.5),
        Dense(1, activation='sigmoid')  # Use 'softmax' and change units if more than two classes
    ])

    # Print model summary
    model.summary()

    # Compile the model
    model.compile(
        loss='binary_crossentropy',  # Use 'categorical_crossentropy' if more than two classes
        optimizer=Adam(),
        metrics=['accuracy']
    )

    # Train the model
    history = model.fit(
        train_generator,
        steps_per_epoch=100,  # Number of batches to process per epoch
        epochs=30,  # Number of epochs to train for
        validation_data=validation_generator,
        validation_steps=50  # Number of validation batches to process
    )

    return model, history

# Example SVM classifier using scikit-learn
def train_svm(train_images, train_labels, test_images, test_labels):
    from sklearn import svm

    classifier = svm.SVC()
    classifier.fit(train_images, train_labels)
    predicted = classifier.predict(test_images)
    return predicted, test_labels
