import cv2

classifier = cv2.CascadeClassifier('data.xml')

cap= cv2.VideoCapture(0)

while True:
    _,img=cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    count=0
    faces=classifier.detectMultiScale(gray,1.1,4)
    prev=1
    for x,y,w,h in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        count+=1
    x=(0,0,0) if count==1 else (0,0,255)
    cv2.putText(img, f"count: {count}", (250,450), cv2.FONT_HERSHEY_COMPLEX,1,x,2)
    cv2.imshow('img',img)
    if prev!=count: 
        print(f"Faces = [{count}]")
        prev=count
    
    if cv2.waitKey(1)==13:break

cap.release()
cv2.destroyAllWindows()
