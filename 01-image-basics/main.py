import cv2

IMAGE_PATH = "sample.jpg"

image = cv2.imread(IMAGE_PATH)

if image is None:
    raise FileNotFoundError(f"Could not read {IMAGE_PATH}")

# Resize while keeping the example simple.
resized = cv2.resize(image, (800, 600))

gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)

# Crop: rows first, then columns.
cropped = resized[100:400, 150:650]

rotated = cv2.rotate(resized, cv2.ROTATE_90_CLOCKWISE)

cv2.imwrite("01-resized.jpg", resized)
cv2.imwrite("02-grayscale.jpg", gray)
cv2.imwrite("03-cropped.jpg", cropped)
cv2.imwrite("04-rotated.jpg", rotated)

print("Created resized, grayscale, cropped, and rotated images.")
