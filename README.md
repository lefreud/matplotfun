# MATPLOT _FUN_

Fun facts:

Make sure new window gets created by using TkInter's backend:
````python
matplotlib.use("TkAgg")
````
https://matplotlib.org/stable/tutorials/introductory/usage.html#the-builtin-backends

Fixing `tkinter module not found` (should happen only on linux):
````shell
sudo apt-get install python3-tk
````

If you are not able to create the mp4 animation file, you need to install ffmpeg and be able to run
```shell
ffmpeg
```


