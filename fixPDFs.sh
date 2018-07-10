cd papers
for i in `find * -name "*.pdf"`;
do
	echo "Processing file $i"
	exiftool -overwrite_original_in_place -TagsFromFile $i 'all<all' ../papers-numbered/papers/$i;
	echo "Done"
done;
cd ..

cd papers-numbered/papers
for i in `find * -name "*.pdf"`;
do
	echo "Linearizing file $i"
	qpdf --linearize $i $i.new;
	mv $i.new $i;
	echo "Done"
done;
cd ..	
