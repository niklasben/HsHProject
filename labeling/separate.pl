#strip of undef and tweets with topics
open (undeffile, ">", "separation/allundefined.txt");
open (topicfile, ">", "separation/alltopics.txt");
open (inputfile, "<", "dataset_labeled/merged.txt");

my @topics  = <inputfile>;

foreach $str (@topics) {
	if ($str =~ m/\bundef\b/i) {print (undeffile $str);}
	if (!($str =~ m/\bundef\b/i)) {print (topicfile $str);}
	}
