import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import time
from collections import deque

# Initialize mediapipe and screen size
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.8, min_tracking_confidence=0.8)

screen_width, screen_height = pyautogui.size()
smoothening = 7
prev_x, prev_y = 0, 0
prev_positions = deque(maxlen=smoothening)

# Capture video
cap = cv2.VideoCapture(0)

while True:
    success, frame = cap.read()
    frame = cv2.flip(frame, 1)  # Flip for mirror effect
    h, w, _ = frame.shape

    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Get landmarks for index finger tip (id 8) and thumb tip (id 4)
            index_finger_tip = hand_landmarks.landmark[8]
            thumb_tip = hand_landmarks.landmark[4]

            x = int(index_finger_tip.x * w)
            y = int(index_finger_tip.y * h)

            screen_x = np.interp(x, (0, w), (0, screen_width))
            screen_y = np.interp(y, (0, h), (0, screen_height))

            # Smooth the cursor movement
            prev_positions.append((screen_x, screen_y))
            avg_x = int(np.mean([pos[0] for pos in prev_positions]))
            avg_y = int(np.mean([pos[1] for pos in prev_positions]))

            pyautogui.moveTo(avg_x, avg_y)

            # Draw landmarks
            mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Calculate distance between index and thumb
            thumb_x, thumb_y = int(thumb_tip.x * w), int(thumb_tip.y * h)
            distance = np.hypot(x - thumb_x, y - thumb_y)

            # If distance is small -> click
            if distance < 40:
                pyautogui.click()
                cv2.circle(frame, (x, y), 15, (0, 255, 0), cv2.FILLED)

            # Show pointer
            cv2.circle(frame, (x, y), 10, (255, 0, 255), -1)

    cv2.imshow("AI Virtual Mouse", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
