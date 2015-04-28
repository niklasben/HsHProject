#!/usr/bin/perl
#### reading file ####
use syntax 'junction';
use Encode qw(encode decode);

#array of stop words
@stop_words = qw(a ab aber ach acht achte achten achter achtes ag alle allein allem allen aller allerdings alles allgemeinen als als also am an andere anderen andern anders au auch auch auf aus ausser ausser ausserdem ausserdem b bald bei beide beiden beim beispiel bekannt bereits besonders besser besten bin bis bisher bist c d da dabei dadurch dafuer dagegen daher dahin dahinter damals damit danach daneben dank dann daran darauf daraus darf darfst darin darueber darum darunter das das dasein daselbst dass dass dasselbe davon davor dazu dazwischen dein deine deinem deiner dem dementsprechend demgegenueber demgemaess demgemaess demselben demzufolge den denen denn denn denselben der deren derjenige derjenigen dermassen dermassen derselbe derselben des deshalb desselben dessen deswegen d.h dich die diejenige diejenigen dies diese dieselbe dieselben diesem diesen dieser dieses dir doch dort drei drin dritte dritten dritter drittes du durch durchaus duerfen duerft durfte durften e eben ebenso ehrlich ei ei, ei, eigen eigene eigenen eigener eigenes ein einander eine einem einen einer eines einige einigen einiger einiges einmal einmal eins elf en ende endlich entweder entweder er Ernst erst erste ersten erster erstes es etwa etwas euch f frueher fuenf fuenfte fuenften fuenfter fuenftes fuer g gab ganz ganze ganzen ganzer ganzes gar gedurft gegen gegenueber gehabt gehen geht gekannt gekonnt gemacht gemocht gemusst genug gerade gern gesagt gesagt geschweige gewesen gewollt geworden gibt ging gleich gott gross gross grosse grosse grossen grossen grosser grosser grosses grosses h habe haben habt hast hat hatte haette hatten haetten heisst her heute hier hin hinter hoch i ich ihm ihn ihnen ihr ihre ihrem ihren ihrer ihres im im immer in in indem infolgedessen ins irgend ist j ja ja jahr jahre jahren je jede jedem jeden jeder jedermann jedermanns jedoch jemand jemandem jemanden jene jenem jenen jener jenes jetzt k kam kann kannst kaum kein keine keinem keinen keiner kleine kleinen kleiner kleines kommen kommt koennen koennt konnte koennte konnten kurz l lang lange lange leicht leide lieber los m machen macht machte mag magst mahn man manche manchem manchen mancher manches mann mehr mein meine meinem meinen meiner meines mensch menschen mich mir mit mittel mochte moechte mochten moegen moeglich moegt morgen muss muss muessen musst muesst musste mussten n na nach nachdem nahm natuerlich neben nein neue neuen neun neunte neunten neunter neuntes nicht nicht nichts nie niemand niemandem niemanden noch nun nun nur o ob ob oben oder oder offen oft oft ohne Ordnung p q r recht rechte rechten rechter rechtes richtig rund s sa sache sagt sagte sah satt Schluss schon sechs sechste sechsten sechster sechstes sehr sei sei seid seien sein seine seinem seinen seiner seines seit seitdem selbst selbst sich sie sieben siebente siebenten siebenter siebentes sind so solang solche solchem solchen solcher solches soll sollen sollte sollten sondern sonst sowie spaeter statt t tag tage tagen tat teil tel tritt trotzdem tun u ueber ueberhaupt uebrigens uhr um und uns unser unsere unserer unter v vergangenen viel viele vielem vielen vielleicht vier vierte vierten vierter viertes vom von vor w wahr waehrend waehrenddem waehrenddessen wann war waere waren wart warum was wegen weil weit weiter weitere weiteren weiteres welche welchem welchen welcher welches wem wen wenig wenig wenige weniger weniges wenigstens wenn wenn wer werde werden werdet wessen wie wie wieder will willst wir wird wirklich wirst wo wohl wollen wollt wollte wollten worden wurde wuerde wurden wuerden x y z zehn zehnte zehnten zehnter zehntes zeit zu zuerst zugleich zum zum zunaechst zur zurueck zusammen zwanzig zwar zwar zwei zweite zweiten zweiter zweites zwischen zwoelf nur hat mal noch ueber war mehr von fuer ab by mir mich was via is wo amp on ob from vor for to at and so zu um gtgt of the zum vom man aber als am an auch auf aus bei bin bis wir bist da dadurch daher darum das dass das dass dass dein deine dem den der des dessen deshalb die dies dieser dieses doch dort du durch ein eine einem einen einer eines er es euer eure fuer hatte hatten hattest hattet hier hinter ich ihr ihre im in ist ja jede jedem jeden jeder jedes jener jenes jetzt kann kannst koennen koennt machen mein meine mit muss musst musst muessen muesst nach nachdem nein nicht nun oder rt st seid sein seine sich sie sind soll sollen sollst sollt sonst soweit sowie wie und unser);

my $dir ='raw';
my $dir_fc = 'cleanedoutput/'; 

$counter = 0;
#function to read in all the data in a specific folder and run the sub function until all data has been written.
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
	#make an array of every line of the file
	@tweets = <file>;
	print file;
	$n = 0;
	
	my @temp_store ;
	
	#start a while loop to go through every line of the array
	while (@tweets[$n]){
		
		@tweets[$n] =~ s///; ### Replace the smileys with words for sentiment analysis
		@tweets[$n] =~ s/@\w*//g; ### Remove the person who retweets
		@tweets[$n] =~ s/[\d\$#@\-~!&*?_()\[\];.,:?^`\\\/]+//g; ### Clean the tweet from unnecessary characters ###
		@tweets[$n] =~ s/(http\w*|httpâ€¦|â€¦|â€)//g; ### Clean tweet from http corpses and Smilies
		
		my @token;
		@token = split("\t",@tweets[$n]); ### Split the tweets by space and generate tokens ###
		
		my @new_token; ### For stop words clean tweet	
			
		if (@token == 4){
			@t = split(" ",@token[3]); #just use the tweets as output
			#### Clean the tweet from stop words ####
			if (scalar @t > 1) {
				
				$m = 0;
				
				while (@t[$m]){
					$word = lc @t[$m]; #make every word lowercase
					$word = encode('utf-8', $word); #replace äöüß with ae ue oe ss
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
						
						if (length($word) > 1) {  	#if the word is bigger than 1 character 
							push(@new_token,$word);		###put it to the end of the array @new_token	
						}
					}		
					$m +=1;
				}
				$tweet= join("\t",@new_token);	### Join the cleaned tweet tokens by tab ###
				if (scalar @new_token > 1 and (none(@temp_store) eq $tweet)) { ###if tweet has more than one word and is not a duplicate
					push(@temp_store, $tweet);
					print (new_file $tweet."\n"); ### Save cleaned tweet in the new file ###
				}	
			}			
		}
		$n += 1;
	}
	close(new_file);
	
}