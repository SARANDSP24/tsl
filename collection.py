import os
import cv2
import time
import uuid

# Define the path and labels
IMAGE_PATH = 'CollectedImages'
labels = ['Hello', 'Yes', 'No', 'Thanks', 'IloveYou', 'Please']
number_of_images = 20

# Ensure the image path directories exist
for label in labels:
    img_path = os.path.join(IMAGE_PATH, label)
    os.makedirs(img_path, exist_ok=True)
    cap = cv2.VideoCapture(0)
    print(f'Press "q" to start collecting images for {label}, "s" to skip, or "e" to end collection.')
    
    while True:
        # Display frame to show camera is ready
        ret, frame = cap.read()
        cv2.imshow('frame', frame)

        # Check for key inputs
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            print(f'Starting collection for {label}...')
            time.sleep(1)
            for imgnum in range(number_of_images):
                ret, frame = cap.read()
                if not ret:
                    print("Failed to capture image")
                    break
                
                # Save the captured frame
                imagename = os.path.join(IMAGE_PATH, label, f'{label}.{str(uuid.uuid1())}.jpg')
                cv2.imwrite(imagename, frame)
                cv2.imshow('frame', frame)
                print(f'Collected image {imgnum+1}/{number_of_images} for {label}')
                time.sleep(2)
                
                # End collection if "e" is pressed
                if cv2.waitKey(1) & 0xFF == ord('e'):
                    print(f'Ending collection for {label}.')
                    break
            break
        elif key == ord('s'):
            print(f'Skipping collection for {label}.')
            break
        elif key == ord('e'):
            print('Ending the entire collection process.')
            cap.release()
            cv2.destroyAllWindows()
            exit()
            
    cap.release()
cv2.destroyAllWindows()
