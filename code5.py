import cv2

# Load pre-trained face detection model from OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Function for face detection in an image
def detect_faces(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    
    return image

# Read an image
image_path = 'path_to_image.jpg'  # Replace with the full path to your image file
image = cv2.imread(image_path)

# Check if the image was read successfully
if image is not None:
    # Perform face detection
    detected_faces_image = detect_faces(image)

    # Display the result
    cv2.imshow('Detected Faces', detected_faces_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Could not read the image. Please check the file path.")
