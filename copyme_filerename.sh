

for fullfile in ~/Documents/Projects/grandev/images/ariana_train/*.jpg; do

	filename=$(basename -- "$fullfile")
	extension="${filename##*.}"
	filename="${filename%.*}"
	prefix='ari_'
	mv "$fullfile" "$prefix$filename"
done

for fullfile in ~/Documents/Projects/grandev/images/nonari_train/*.jpg; do

	filename=$(basename -- "$fullfile")
	extension="${filename##*.}"
	filename="${filename%.*}"
	prefix='nonari_'
	mv "$fullfile" "$prefix$filename"
done
