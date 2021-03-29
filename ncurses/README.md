# ncurses

## git
https://github.com/cpressey/ncurses_programs.git  

## 程序架构

```c
/*File Name: hello.c*/
#include <ncurses>  // -lncurses 已经包含stdio.h

int main()
{
    initscr(); /*初始化，进入ncurses模式*/
    printw("hello world!"); /*在虚拟屏幕上打印*/
    refresh(); /*将虚机屏幕上的内容写入显示器，并刷新*/
    getchar(); /*等待用户输入*/
    endwin();

    return 0;
}

// gcc hello.c -o hello -lncurese
```

## initscr() 函数调用后的初始化函数

- raw() cbreak()  禁止行缓冲函数
- echo noecho 控制是否将从键盘输入的字符显示在终端上
- keypad 功能键函数
- halfdelay 半延时模式，处理超时

```c
#include<ncurses.h>
int main(){
    int ch;
    initscr(); /*开始curses模式*/
    raw();/*禁用行缓冲*/
    keypad(stdscr,TRUE);/*开启功能键响应模式*/
    noecho();/*当执行getch()函数的时候关闭键盘回显*/
    printw("Typeanycharactertoseeitinbold\n");
    ch=getch();/*如果没有调用raw()函数，我们必须按下enter键才可以将字符传递给程序*/

    if(ch==KEY_F(1))/*如果没有调用keyiad（）初始化，将不会执行这条语句*/
        printw("F1Keypressed");/*如果没有使用noecho()函数，一些控制字符将会被打印到屏幕上*/
    else {
        printw("Thepressedkeyis");
        attron(A_BOLD);  /*修饰开头 - BOLD粗体*/
        printw("%c",ch);
        attroff(A_BOLD); /*修饰结尾*/
    }
    refresh();/*将缓冲区的内容打印到显示器上*/
    getch();/*等待用户输入*/
    endwin();/*结束curses模式*/
    return 0;
}
    

```

## 窗口机制简介
```c
printw(string); /*在stdscr的当前光标位置打印字符串string*/
mvprintw(y,x,string); /*将字符串string打印在坐标(y,x)处*/
wprintw(win,string); /*在窗口win的当前光标位置打印字符串string*/
mvwprintw(win,y,x,string); /*将光标移动到窗口win的(y,x)坐标处然后打印字符串string*/
```
## 输出函数
1. addch   # 输出单字符
2. printw  # 格式化输出
3. addstr  # 打印字符串

```c
addch(ch|A_BOLD|A_UNDERLINE);  /*ch 粗体、下划线 */
//attrset()、attron()、attroff()修饰函数
//mvwaddch()函数是把光标移动到指定窗口中的指定位置处输出字符。

```
