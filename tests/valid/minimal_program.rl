topology {
  roles { r1 { count: 1 } r2 { count: 1 } }
  links { r1 -- r2 }
}
routing {
  bgp {
    asn { r1: 65001  r2: 65002 }
    neighbors: auto
  }
}
policy {
  define P {
    permit { match any }
  }
}
intent {
  I1: route t {
    primary: r1 >> r2
  }
}