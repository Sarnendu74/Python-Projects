import cv2

try:
    # Prompt the user for the image path
    image_path = input('Enter your image path: ')
    
    # Fetching the photo
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError("Image not found. Please check the path and try again.")
    
    # Get dimensions for resizing
    width = int(input('Enter your width: '))
    height = int(input('Enter your height: '))
    
    # Resizing the image
    resized_image = cv2.resize(image, (width, height))
    
    # Save the resized image
    resized_image_path = f"{image_path.rsplit('.', 1)[0]}_resized.jpg"
    cv2.imwrite(resized_image_path, resized_image)
    
    # Display the resized image
    cv2.imshow('Resized_Version', resized_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  # Ensure all windows are closed properly

    print(f'Your photo has been resized successfully and saved as: {resized_image_path}')
    print('Thank You for using the Photo Resizing tool!')
except FileNotFoundError as fnf_error:
    print(fnf_error)
except ValueError:
    print("Invalid input! Please enter numeric values for width and height.")
except Exception as e:
    print(f"An error occurred: {e}")
