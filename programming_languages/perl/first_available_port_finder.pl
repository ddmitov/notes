#!/usr/bin/perl

# Based on: https://gist.github.com/rkulla/1116085

# ./first_available_port_finder.pl [start port] [stop port]

use Socket;

my ($ip, $protocol, $port, $stop_port, $first_available_port, $myhouse, $yourhouse);
$ip = "localhost";
$protocol = getprotobyname('tcp');

($port, $stop_port) = @ARGV;

$port = 1 if not $port;
$stop_port = 1024 if not $stop_port;

until ($port == $stop_port + 1) {
    socket(SOCKET, PF_INET, SOCK_STREAM, $protocol);
    $yourhouse = inet_aton($ip);
    $myhouse = sockaddr_in($port, $yourhouse);

    if (!connect(SOCKET, $myhouse)) {
        unless ($first_available_port) {
          $first_available_port = $port;
          last;
        }
    } else {
        close SOCKET || die "close: $!";
    }

    $port ++;
}

if ($first_available_port) {
  print "First available port: $first_available_port\n";
}
