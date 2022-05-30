import Tkinter
import tkMessageBox
import speedtest

top = Tkinter.Tk()

def SpeedTest():   	
   	speed_test = speedtest.Speedtest()
	download_speed = st.download()
	tkMessageBox.showinfo("Your Download speed is", download_speed) 
	upload_speed = st.upload()
	print("Your Upload speed is", upload_speed)
	def bytes_to_mb(bytes):
  		KB = 1024
  		MB = KB * 1024
  	return int(bytes/MB)
	val = bytes_to_mb(1024 * 1024)
	print(val)
	download_speed = bytes_to_mb(st.download())
	tkMessageBox.showinfo("Your Download speed is", download_speed)

B = Tkinter.Button(top, text ="Run Speed Test", command = SpeedTest)

B.pack()
top.mainloop()