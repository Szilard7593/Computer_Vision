import cv2
import mediapipe as mp


def run_hand_tracker():
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    mp_drawing_styles = mp.solutions.drawing_styles

    cam = cv2.VideoCapture(0)

    with mp_hands.Hands(
            model_complexity=0,
            max_num_hands=2,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
    ) as hands:
        while cam.isOpened():
            success, frame = cam.read()
            if not success:
                print("Empty frame")
                continue

            frame = cv2.flip(frame, 1)

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            #procesam imaginea
            results = hands.process(frame_rgb)

            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    #ca sa desenam peste video-ul live, peste fiecare frame
                    mp_drawing.draw_landmarks(
                        image=frame,
                        landmark_list=hand_landmarks,
                        connections=mp_hands.HAND_CONNECTIONS,
                        # CHANGED: Corrected style calls
                        landmark_drawing_spec=mp_drawing_styles.get_default_hand_landmarks_style(),
                        connection_drawing_spec=mp_drawing_styles.get_default_hand_connections_style(),
                    )

            #afisam
            cv2.imshow("Hand Tracking", frame)

            #verificam input-ul de ca tastura in caz ca de ii 1 sau q inchidem
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cam.release() #inchidem camera
        cv2.destroyAllWindows() #inchidem pop-ul


if __name__ == "__main__":
    run_hand_tracker()
