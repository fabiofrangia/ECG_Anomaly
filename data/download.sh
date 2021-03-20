url=https://archive.physionet.org/challenge/2017/

curl -O $url/training2017.zip
unzip training2017.zip
rm -rf training2017.zip
curl -O $url/sample2017.zip
unzip sample2017.zip
rm -rf sample2017.zip
curl -O $url/REFERENCE-V.csv
