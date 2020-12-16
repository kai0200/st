#!/usr/bin/env bash

# 如果是多个目录的文件，把目录放在ditectorys这个目录下
DIR=directorys


function do_dir() {
  # pdf to html
  dirname="$DIR/$1"
  for file in $(ls $dirname/*.pdf)
  do
    name=$(echo "$file"|awk -F. '{print $1}')
    echo "......$name.pdf to $name.html "
    pdftotree "$file" > "$name.html"
  done

  # html all in one
  [ -d "$dirname/xlsx" ] || mkdir "$dirname/xlsx"

  echo "All html in $dirname/xlsx/out.html...."
  echo "<html>" >  $dirname/xlsx/out.html

  for html in $(ls $dirname/*.html)
  do
    sed -i 's/<html>//g' $html 2&>1 &
    sed -i 's/<\/html>//g' $html 2&>1 &
    cat $html >> $dirname/xlsx/out.html
  done
  echo "</html>" >>  $dirname/xlsx/out.html

  # all html to xlsx
  echo "Transformate HTML to XLSX in $dirname/xlsx/$1-out.xlsx...... "
  python3 get-html-table.py $dirname/xlsx/out.html > $dirname/xlsx/"$1-out.xlsx"

}

# pro_dir 代表directorys 下的项目目录
for pro_dir in $(ls "$DIR")
do
  do_dir "$pro_dir"
done
