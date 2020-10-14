# 修改键盘位置 - manjaro

###  操作
yay -S xorg
xmodmap  
xmodmap -pke

xmodmap -pke > ~/.xmodmap

xev 按键 kecode

vim ~/.xmodmap 

开头增加
clear control
clear lock
clear mod1

结尾增加
add control = Control_L Control_R
add mod1 = Alt_L

xmodmap ~/.xmodmap

screenkey # 屏显键置







