from fer import FER
import cv2

maxi = 1
most = ''
array = []
detector = FER(mtcnn=True)
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    result = detector.detect_emotions(frame)
    for face in result:
        x, y, w, h = face['box']
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        emotion, score = detector.top_emotion(frame)
        cv2.putText(frame, str(emotion), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        array.append(str(emotion))
    cv2.imshow("Detector", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
for x in array:
    if x == 'None':
        array.remove('None')
if array.count('neutral') > maxi:
        maxi = array.count('neutral')
        most = 'neutral'
elif array.count('happy') > maxi:
        maxi = array.count('happy')
        most = 'happy'
elif array.count('sad') > maxi:
        maxi = array.count('sad')
        most = 'sad'
elif array.count('angry') > maxi:
        maxi = array.count('sad')
        most = 'angry'
elif array.count('surprise') > maxi:
        maxi = array.count('surprise')
        most = 'surprise'
print(most)