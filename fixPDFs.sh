cd papers
for i in `find * -name "*.pdf"`;
do
	echo "Processing file $i (../papers-numbered/papers/$i)"
	exiftool -overwrite_original_in_place -TagsFromFile $i '-xmp:all<all' ../papers-numbered/papers/$i;
	echo "Done"
done;
cd ..

cd papers-numbered
for i in `find * -name "*.pdf"`;
do
	echo "Linearizing file $i"
	qpdf --linearize $i $i.new;
	mv $i.new $i;
	echo "Done"
done;
cd ..	
