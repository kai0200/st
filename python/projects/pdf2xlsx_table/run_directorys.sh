#!/usr/bin/env bash

# 如果是多个目录的文件，把目录放在ditectorys这个目录下
DIR=directorys


function do_dir() {
  # pdf to html
  dirname="$DIR/$1"
  for file in $(ls "$dirname/*.pdf")
  do
    name=$(echo "$file"|awk -F. '{print $1}')
    echo "......$name.pdf to $name.html "
    pdftotree "$file" > "$name.html"
  done

  # html all in one
  [ -d "$dirname/xlsx"] || mkdir "$dirname/xlsx"
  echo "All html in $dianem/xlsx/out.html...."
  echo "<html>" >  $dirname/xlsx/out.html
  for html in $(ls $dirname/*.html)
  do
    sed -i 's/<html>//g' $html
    sed -i 's/<\/html>//g' $html
    cat $html >> $dirname/xlsx/out.html
  done
  echo "</html>" >>  $dirname/xlsx/out.html

  # all html to xlsx
  echo "Transformate HTML to XLSX in xlsx/$out_file...... "
  python3 get-html-table.py $dirname/xlsx/out.html > $dirname/xlsx/"$1-out.xlsx"

}

for pro_dir in $(ls "$DIR")
do
  do_dir "$pro_dir"
done
