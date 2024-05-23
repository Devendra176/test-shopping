use strict;
use warnings;

my @xor_order;
foreach my $e(0..length($ARGV[0])-1){
    push @xor_order, unpack('H*', pack('a*', substr($ARGV[0], $e, 1)) ^ pack('H*', "61"));
}
my $raw = join '', @xor_order;
my $final = pack "h*", $raw;
print "$final\n";