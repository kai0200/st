#!/usr/bin/env bash

OUT=$OUT

# pdf to html
for file in $(ls files/*.pdf)
do
  name=$(echo "$file"|awk -F. '{print $1}')
  echo "......$name.pdf to $name.html "
  pdftotree "$file" > "$name.html"
done

# html all in one
echo "All html in xlsx/out.html...."
echo "<html>" >  xlsx/out.html
for html in $(ls files/*.html)
do
  sed -i 's/<html>//g' $html
  sed -i 's/<\/html>//g' $html
  cat $html >> xlsx/out.html
done
echo "</html>" >>  xlsx/out.html

# all html to xlsx
echo "Transformate HTML to XLSX in xlsx/$OUT...... "
python3 get-html-table.py xlsx/out.html > xlsx/$OUT
