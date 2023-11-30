import cv2


video = cv2.VideoCapture("./AnthonyShkraba.mp4")

if video.isOpened()== False:
    print("Não foi possível carregar o vídeo")


height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
fps = int(video.get(cv2.CAP_PROP_FPS))

output = cv2.VideoWriter("Boxing.mp4",cv2.VideoWriter_fourcc(*'DIVX'),5,(width,height))

while True:
    #Capturar o quadro do vídeo
    ret, frame = video.read()

    #Exibir o quadro
    cv2.imshow("Web Cam", frame)

    output.write(frame)

    #encerrar o vídeo se espaço for pressionado
    if cv2.waitKey(25) == 32:
        break

#Libera o objeto de captura do vídeo
video.release()
output.release()

#Fecha todas as janelas
cv2.destroyAllWindows()
