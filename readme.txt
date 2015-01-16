執行方式：bash pig.sh
用UDF function(python)寫分割json檔，回傳作者的名字
在pig檔中計算作者出現次數，然後排序、取前100名
最後的結果輸出在output/part-r-00000