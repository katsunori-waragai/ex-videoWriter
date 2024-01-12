```commandline
waragai@waragai-orin:~/github/ex-videoWriter$ python video_player.py 2024-01-12-140709.webm 
Gtk-Message: 15:35:13.024: Failed to load module "canberra-gtk-module"
```

```commandline
sudo apt-get install libcanberra-gtk*
```

で解決した。
