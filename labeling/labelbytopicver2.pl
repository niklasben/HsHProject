###Last Problem: What to do with tweets that are labeled with two topics an no topic is dominant.###

use syntax 'junction';

	###Initialise variables###
my $dir ='C:/Strawberry/perl/bin/dataset';
my $dir_fc = 'C:/Strawberry/perl/bin/dataset_labeled/'; 
my $i = 0;
	
	###Hash with all words for labeling the tweets. Left side: Keyword, Right side: Topic###
my %topiclist = ("Urlaub" => "Urlaub", "Reisen" => "Urlaub", "Hotels" => "Urlaub", "Flug" => "Urlaub", "Medizin" => "Medizin", "England" => "England", "London" => "England");

	###Foreach-Loop to grab all files in the desired Folder.###
foreach my $fp (glob($dir."/*.txt")) {
	open(file, "<", $fp);
	my @path_name = split('/', $fp);
	my $name = @path_name[scalar @path_name - 1];
	open(new_file, ">", $dir_fc.$name);
	labelByTopic(file, new_file);
	close(file);
}

	###subroutine for Labeling###
sub labelByTopic(file,new_file) {
	
	my @tweets = <file>;
		
		foreach my $line (@tweets) {
			$line = lc $line;	
			my @token = split("\t",$line); ###Make Tokens for every word in $line
			foreach $key (keys %topiclist) {
				$i = 0;
				for ($i; $i < scalar @token + 1; $i++) { ###Go through every single token and match it with every single key in %topiclist.
					if (@token[$i] =~ /$key/gi) {
						my @topi = push(@topi ,$topiclist{$key}); ###If there is a match, add the Topic to the @topi array.	
					}
				}
			}
			
			@topi = sort @topi; ###Sort the @topi array.
			my $topica = join("\t",@topi); ###"England\tEngland\tUrlaub" Now it looks like that.
			
			if (scalar @topi > 1) { ###if the @topi array has more than 1 entry.
			
				foreach my $keys (@topi) { ###Count every word.
					$HASH{$keys}++ ;
				}
			
				foreach $keys (keys %HASH) {
					if ($HASH{$keys}>1) { ###If a topic exists multiple times...
						my $val = (sort { $HASH{$b} <=> $HASH{$a} } keys %HASH)[0]; ###...get the highest valued topic...
						$topica = $val; ###...and give it to $topica, which is the final label.
					}
					$HASH{$keys} = ();	
				}
			}
			
			if (!@topi) { ###If no Topics were found, set the final label to undef.
				$topica = "undef";
			}
			
			print (new_file $topica."\t". $line); ###Print the file with the topic.
			@topi = (); ###Reset the @topi array.
		}
}