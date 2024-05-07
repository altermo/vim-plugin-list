pushd .
cd ..
cat raw|sed 's/https:\/\/github.com\///g'|tr '[:upper:]' '[:lower:]'|sort -u > raw_temp
cp raw (mktemp)
mv raw_temp raw
popd
