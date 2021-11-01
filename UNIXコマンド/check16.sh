wc -l ./div/0.txt
wc -l ./div/1.txt
wc -l ./div/2.txt
wc -l ./div/3.txt
wc -l ./div/4.txt

cat ./div/0.txt ./div/1.txt ./div/2.txt ./div/3.txt ./div/4.txt > join.txt
diff -q --strip-trailing-cr join.txt popular-names.txt
rm join.txt
