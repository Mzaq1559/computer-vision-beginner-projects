import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise RuntimeError("Could not open webcam")

previous_gray = None

while True:
    success, frame = cap.read()
    if not success:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if previous_gray is None:
        previous_gray = gray
        continue

    difference = cv2.absdiff(previous_gray, gray)
    threshold = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)[1]
    threshold = cv2.dilate(threshold, None, iterations=2)

    contours, _ = cv2.findContours(
        threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )

    moving_objects = 0

    for contour in contours:
        if cv2.contourArea(contour) < 1000:
            continue

        x, y, width, height = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)
        moving_objects += 1

    cv2.putText(
        frame,
        f"Motion regions: {moving_objects}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 0),
        2,
    )

    cv2.imshow("Motion Detection", frame)
    cv2.imshow("Difference", threshold)

    previous_gray = gray

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
