STR="GO"
python systm/dgjkhe82y/tmp/check1.py > systm/dgjkhe82y/tmp/output1.txt
if [ $? != 0 ]; then
     STR="STOP"
fi
python systm/dgjkhe82y/tmp/check2.py > systm/dgjkhe82y/tmp/output2.txt
if [ $? != 0 ]; then
     STR="STOP"
fi
python systm/dgjkhe82y/tmp/check3.py > systm/dgjkhe82y/tmp/output3.txt
if [ $? != 0 ]; then
     STR="STOP"
fi
python systm/dgjkhe82y/tmp/check4.py > systm/dgjkhe82y/tmp/output4.txt
if [ $? != 0 ]; then
     STR="STOP"
fi
python systm/dgjkhe82y/tmp/check5.py > systm/dgjkhe82y/tmp/output5.txt
if [ $? != 0 ]; then
     STR="STOP"
fi
python systm/dgjkhe82y/tmp/check6.py > systm/dgjkhe82y/tmp/output6.txt
if [ $? != 0 ]; then
     STR="STOP"
fi
python systm/dgjkhe82y/tmp/check7.py > systm/dgjkhe82y/tmp/output7.txt
if [ $? != 0 ]; then
     STR="STOP"
fi
python systm/dgjkhe82y/tmp/check8.py > systm/dgjkhe82y/tmp/output8.txt
if [ $? != 0 ]; then
     STR="STOP"
fi
python systm/dgjkhe82y/tmp/check9.py > systm/dgjkhe82y/tmp/output9.txt
if [ $? != 0 ]; then
     STR="STOP"
fi
python systm/dgjkhe82y/tmp/check10.py > systm/dgjkhe82y/tmp/output10.txt
if [ $? != 0 ]; then
     STR="STOP"
fi
python systm/dgjkhe82y/tmp/check11.py > systm/dgjkhe82y/tmp/output11.txt
if [ $? != 0 ]; then
     STR="STOP"
fi
python systm/dgjkhe82y/tmp/check12.py > systm/dgjkhe82y/tmp/output12.txt
if [ $? != 0 ]; then
     STR="STOP"
fi
python systm/dgjkhe82y/tmp/check13.py > systm/dgjkhe82y/tmp/output13.txt
if [ $? != 0 ]; then
     STR="STOP"
fi
python systm/dgjkhe82y/tmp/check14.py > systm/dgjkhe82y/tmp/output14.txt
if [ $? != 0 ]; then
     STR="STOP"
fi
python systm/dgjkhe82y/tmp/check15.py > systm/dgjkhe82y/tmp/output15.txt
if [ $? != 0 ]; then
     STR="STOP"
fi
python systm/dgjkhe82y/tmp/check16.py > systm/dgjkhe82y/tmp/output16.txt
if [ $? != 0 ]; then
     STR="STOP"
fi
python systm/dgjkhe82y/tmp/check17.py > systm/dgjkhe82y/tmp/output17.txt
if [ $? != 0 ]; then
     STR="STOP"
fi
python systm/dgjkhe82y/tmp/check18.py > systm/dgjkhe82y/tmp/output18.txt
if [ $? != 0 ]; then
     STR="STOP"
fi
if [ $STR = "GO" ];then
   bash systm/dgjkhe82y/2b.sh
else
   clear
cat systm/dgjkhe82y/tmp/summary0.txt >systm/dgjkhe82y/tmp/summary.txt
cat systm/dgjkhe82y/tmp/summary1.txt >>systm/dgjkhe82y/tmp/summary.txt
cat systm/dgjkhe82y/tmp/summary.txt > reports/330smallest.txt
cat systm/dgjkhe82y/tmp/summary.txt > systm/dgjkhe82y/zbkupc/330smallest/330smallest.txt
cat systm/dgjkhe82y/tmp/summary.txt > systm/dgjkhe82y/zbkupc/330smallest/231021-160512.txt
cat 330smallest.py > systm/dgjkhe82y/zbkupc/330smallest/231021-160512.bkp
cat systm/dgjkhe82y/tmp/summary.txt

fi