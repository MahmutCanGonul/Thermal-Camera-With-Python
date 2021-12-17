def thermal_camera():
    print("If you want exit enter the 'esc' keyword.")
    video = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    video.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter.fourcc('Y','1','6',' '))
    video.set(cv2.CAP_PROP_CONVERT_RGB, 0)

    if video.isOpened(): # try to get the first frame
       rval, frame = video.read()
    else:
       rval = False

 
    
    while rval:
    # Get a Region of Interest slice - ignore the last 3 rows. 
       frame_roi = frame[:-3, :]

    # Normalizing frame to range [0, 255], and get the result as type uint8.
       normed = cv2.normalize(frame_roi, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

     
     
    # CLAHE supposed to work with uint16 -  so we use np.uint8 in cv2.normalize
       
       """
       cl1 = clahe.apply(ex)
       """
       nor = cv2.cvtColor(np.uint8(normed), cv2.COLOR_BGR2HSV)  # Convert gray-scale to BGR (no really needed).

       cv2.imshow("camera", cv2.resize(nor, dsize=(640, 480), interpolation=cv2.INTER_LINEAR))
       key = cv2.waitKey(1)
       if key == 27: # exit on ESC
          cv2.destroyAllWindows()
          video.release()
          break

    # Grab the next frame from the camera.
       rval, frame = video.read()
    
    
    thermal_camera()
    
    
    
    
