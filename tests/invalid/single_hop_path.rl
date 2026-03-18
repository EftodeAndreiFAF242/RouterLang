topology { roles { r1 { count: 1 } } links { r1 -- r1 } } 
routing { bgp { asn { r1: 65001 } neighbors: auto } } 
policy { define P { permit { match any } } } 
intent { I1: route t { primary: r1 } } 
