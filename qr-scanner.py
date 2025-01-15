import cv2
from pyzbar.pyzbar import decode

def qr_code_scanner():
    # Open the webcam
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)  # Set the width of the webcam feed
    cap.set(4, 480)  # Set the height of the webcam feed

    print("Press 'q' to quit.")

    while True:
        # Read the frame from the webcam
        ret, frame = cap.read()

        if not ret:
            print("Failed to capture video frame.")
            break

        # Decode QR codes in the frame
        decoded_objects = decode(frame)

        for obj in decoded_objects:
            # Get the QR code data
            qr_data = obj.data.decode('utf-8')
            qr_type = obj.type
            print(f"Detected {qr_type}: {qr_data}")

            # Draw a rectangle around the QR code
            points = obj.polygon
            if len(points) > 4:  # Adjust for irregular QR code shapes
                hull = cv2.convexHull(points)
                points = hull

            for i in range(len(points)):
                pt1 = points[i]
                pt2 = points[(i + 1) % len(points)]
                cv2.line(frame, (pt1.x, pt1.y), (pt2.x, pt2.y), (0, 255, 0), 2)

            # Display the QR code data on the frame
            cv2.putText(frame, qr_data, (obj.rect.left, obj.rect.top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

        # Display the frame
        cv2.imshow("QR Code Scanner", frame)

        # Quit if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    qr_code_scanner()
