###Last Problem: What to do with tweets that are labeled with two topics and no topic is dominant.###
###Solved: The script now only takes the first topic.###

###Update: Words can only be at the beginning or at the end of a composite word. It provides better solutions after all.###
###Update2: The topiclist can now be provided in a txt file.###

use syntax 'junction';

	###Initialise variables###
my $dir ='dataset';
my $dir_fc = 'dataset_labeled/'; 
my $i = 0;
my %topiclist = (); ###Hash with all words for labeling the tweets. Left side: Keyword, Right side: Topic

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
	
	open(topiclist, "<", "topics/topiclist.txt"); ### Open the Topiclist
	
	my @topics = <topiclist>;
	
		foreach my $topicline (@topics) {
			my @word = split("\t",$topicline);
			my $value = @word[0]; ###Value is the first word in every line.
			chomp(@word[-1]); ###Chomp the \n at the end of the line.
				for ($i = 1; $i < scalar @word + 1; $i++) {
					$topiclist{@word[$i]} = $value;
				}
		}
		delete $topiclist {""}; ###Somehow there is a key with nothing in it, so delete it afterwards.
	
	my @tweets = <file>;
		
		foreach my $line (@tweets) {
			$line = lc $line;	
			my @token = split("\t",$line); ###Make Tokens for every word in $line
				foreach $key (keys %topiclist) {
					$i = 0;
						for ($i; $i < scalar @token + 1; $i++) { ###Go through every single token and match it with every single key in %topiclist.
							if (@token[$i] =~ /^($key)|($key\w{0,3})$/i) { ###The regular Expression says: $key only at the beginning or at the end with 3 optional characters after the key for flection suffixes.
								my @topi = push(@topi ,$topiclist{$key}); ###If there is a match, add the Topic to the @topi array.
						}
					}
				}
			
			my $topica = @topi[0] if (@topi); ### NEW CODE Take only the first topic if there is a @topi array.
			#my $topica = join("\t",@topi); ###"England\tEngland\tUrlaub" Now it looks like that. OLD CODE to grab all topics.
			
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