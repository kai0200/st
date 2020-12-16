#!/usr/bin/env bash
OUT=out.txt

[ -d files ] || mkdir files
[ -d text ] || mkdir text

# pdf to html
for file in $(ls files/*.pdf)
do
  name=$(echo "$file"|awk -F. '{print $1}')
  echo "......$name.pdf to $name.html"
  pdftotree "$file" > "$name.html"
done

# html all in one
echo "All html in text/$OUT...."

cat /dev/null > text/"$OUT"
for html in $(ls files/*.html)
do
  python3 get-html-text.py $html >> text/"$OUT"
done
