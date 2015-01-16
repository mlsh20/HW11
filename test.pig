Register 'spl.py' using jython as myfuncs;
A = load '$input';
B = foreach A generate flatten(myfuncs.splitJson((chararray)$0)) as word;
C = group B by word;
D = foreach C generate COUNT(B) as count, group;
E = order D by count desc;
F = limit E 100;
store F into '$output';
