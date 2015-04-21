#!/usr/bin/perl
#### reading file ####
use syntax 'junction';
use Encode qw(encode decode);

my $dir_ip ='C:/Strawberry/twitter/input/';		# Directory Input
my $dir_op = 'C:/Strawberry/twitter/output/';	# Directory Output
my $dir_sa = 'C:/Strawberry/twitte/analysis/';	# Directory Sentiment Analysis Libraries

$counter = 0;

foreach my $fp (glob($dir_ip."/*.txt")) {
	$counter += 1;
	print ($counter."\n");
	open(file, "<", $fp);
	print($fp." completed\n");
	@path_name = split('/', $fp);
	$name = @path_name[scalar @path_name - 1];
	open(new_file, ">", $dir_fop.$name);
	analysis(file, new_file);
	close(file);
}




$string = "input_strings_here";		# Input each line as String
if ($string =~ m/input_words_here/)	# Input each pos/neg/neutral word
	{
		print "ausgabe_true";		# Output TRUE
	}
else
	{
		print "output_false";		# Output FALSE
	}