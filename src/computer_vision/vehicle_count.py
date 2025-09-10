# ... (your existing imports and setup code) ...
import requests
import time

# ... (model loading and video capture setup) ...
API_URL = "http://your-backend-api.com/vehicle-data" 

last_sent_time = time.time()
vehicle_count = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame, classes=[2, 3, 5, 7])
    
    # Get the count for the current frame
    current_count = len(results[0].boxes)
    vehicle_count = current_count # Use the most recent count

    annotated_frame = results[0].plot()
    
    cv2.putText(annotated_frame, f"Vehicles: {vehicle_count}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Check if 5 seconds have elapsed
    if time.time() - last_sent_time >= 5:
        send_data(vehicle_count)
        last_sent_time = time.time()

    cv2.imshow('Vehicle Detection', annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ... (release resources) ...
