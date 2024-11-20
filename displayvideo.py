import cv2
import numpy as np

width, height, fps = 960, 540, 30
filename = "RGB/WalkingStaticBackground.rgb"


with open(filename, "rb") as file:
    while True:
        # Read one frame
        frame_data = file.read(width * height * 3)
        if not frame_data:
            break

        
        frame = np.frombuffer(frame_data, dtype=np.uint8).reshape((height, width, 3))

        #convert to BGR from RGB
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    
        cv2.imshow("RGB Video", frame)

        # Wait for frame duration
        if cv2.waitKey(int(1000 / fps)) == 27: 
            break

cv2.destroyAllWindows()
