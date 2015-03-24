#!/usr/bin/perl
#### reading file ####
use syntax 'junction';
use Encode qw(encode decode);

@stop_words = qw(nur hat mal noch ueber war mehr von fuer ab by mir mich was via is wo amp on ob from vor for to at and so zu um gtgt of the zum vom man aber als am an auch auf aus bei bin bis wir bist da dadurch daher darum das daß dass dein deine dem den der des dessen deshalb die dies dieser dieses doch dort du durch ein eine einem einen einer eines er es euer eure für hatte hattenhattest hattet hier hinter ich ihr ihre im in ist ja jede jedem jeden jeder jedes jener jenes jetzt kann kannst können könnt machen mein meine mit muß mußt musst müssen müßt nach nachdem nein nicht nun oder rt st seid sein seine sich sie sind soll sollen sollst sollt sonst soweit sowie wie und unser);

my $dir ='C:/Strawberry/perl/bin/Output';
my $dir_fc = 'C:/Strawberry/perl/bin/cleanedoutput/'; 

$counter = 0;

foreach my $fp (glob($dir."/*.txt")) {
	$counter += 1;
	print ($counter."\n");
	open(file, "<", $fp);
	print($fp." completed\n");
	@path_name = split('/', $fp);
	$name = @path_name[scalar @path_name - 1];
	open(new_file, ">", $dir_fc.$name);
	datacleaning(file, new_file);
	close(file);
}

sub datacleaning(file, new_file) {
	@tweets = <file>;
	print file;
	$n = 0;
	
	my @temp_store ;
	
	while (@tweets[$n]){
		
		@tweets[$n] =~ s/@\w*//g; ### Remove the person who retweets
		@tweets[$n] =~ s/[\d\$#@\-~!&*?_()\[\];.,:?^`\\\/]+//g; ### Clean the tweet from unnecessary characters ###
		@tweets[$n] =~ s/(http\w*|httpâ€¦|â€¦|â€)//g; ### Clean tweet from http corpses and Smilies
		
		my @token;
		@token = split("\t",@tweets[$n]); ### Split the tweets by space and generate tokens ###
		
		my @new_token; ### For stop words clean tweet	
			
		if (@token == 4){
			@t = split(" ",@token[3]);
			#### Clean the tweet from stop words ####
			if (scalar @t > 1) {
				
				$m = 0;
				
				while (@t[$m]){
					$word = lc @t[$m];
					$word = encode('utf-8', $word);
						$word =~ s/ä/ae/g;
						$word =~ s/ü/ue/g;
						$word =~ s/ö/oe/g;
						$word =~ s/Ä/Ae/g;
						$word =~ s/Ü/Ue/g;
						$word =~ s/Ö/Oe/g;
						$word =~ s/Ã¤/ae/g;  
						$word =~ s/Ã¼/ue/g;
						$word =~ s/ÃŸ/ss/g;
						$word =~ s/ß/ss/g;
						$word =~ s/\W//g;
					if (none(@stop_words) eq $word){ ### Check each words if it is available in the stop words list ###
						
						if (length($word) > 1) {  	
							push(@new_token,$word);			
						}
					}		
					$m +=1;
				}
				$tweet= join("\t",@new_token);	### Join the cleaned tweet tokens by tab ###
				if (scalar @new_token > 1 and (none(@temp_store) eq $tweet)) {
					push(@temp_store, $tweet);
					
					print (new_file $tweet."\n"); ### Save cleaned tweet in the new file ###
				}	
			}			
		}
		$n += 1;
	}
	close(new_file);
	
}