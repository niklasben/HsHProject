use syntax 'junction';

my $dir ='C:/Strawberry/perl/bin/dataset';
my $dir_fc = 'C:/Strawberry/perl/bin/dataset_labeled/'; 

my $counter = 0;
my %topiclist = ("Urlaub" => "Urlaub", "Reisen" => "Urlaub", "Hotels" => "Urlaub", "Flug" => "Urlaub", "Medizin" => "Medizin");

foreach my $fp (glob($dir."/*.txt")) {
	open(file, "<", $fp);
	my @path_name = split('/', $fp);
	my $name = @path_name[scalar @path_name - 1];
	open(new_file, ">", $dir_fc.$name);
	labelByTopic(file, new_file);
	close(file);
}

sub labelByTopic(file,new_file) {
	my @tweets = <file>;
		foreach my $line (@tweets) {
			$line = lc $line;	
			foreach $key (keys %topiclist) {
				if ($line =~ /$key/gi) {
					print (new_file $topiclist{$key}."\t".$line);
				}
			}
		}
}