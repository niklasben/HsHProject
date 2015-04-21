#!usr/bin/perl
use strict;
use warnings;

my $dir_ip ='C:/Strawberry/twitter/input/';		# Directory Input
my $dir_op = 'C:/Strawberry/twitter/output/';	# Directory Output
my $dir_sa = 'C:/Strawberry/twitte/analysis/';	# Directory Sentiment Analysis Libraries

#Lexical variable for filehandle is preferred, and always error check opens.
open my $keywords_pos,    '<', 'C:/Strawberry/twitte/analysis/positive.tsv' or die "Can't open keywords: $!";
open my $search_file, '<', 'C:/Strawberry/twitter/output/search.txt'   or die "Can't open search file: $!";

my $keyword_or = join '|', map {chomp;qr/\Q$_\E/} <$keywords_pos>;
my $regex = qr|\b($keyword_or)\b|;

while (<$search_file>)
{
    while (/$regex/g)
    {
        print "$.: $1\n";
    }
}