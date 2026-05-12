topology {
  roles {
    spine  { count: 2 }
    leaf   { count: 4 }
    edge   { count: 2 }
  }
  links {
    spine -- leaf  { weight: 1 }
    spine -- edge  { weight: 2 }
    edge  -- leaf  { weight: 3 }
  }
  devices {
    spine: [R-SPINE-1, R-SPINE-2]
    leaf:  [R-LEAF-1, R-LEAF-2, R-LEAF-3, R-LEAF-4]
    edge:  [R-EDGE-1, R-EDGE-2]
  }
}
routing {
  bgp {
    asn {
      spine: 65001
      leaf:  65002
      edge:  65003
    }
    neighbors: auto
    route-reflector: spine
  }
  ospf {
    area 0 { roles: [spine, leaf] }
    area 1 { roles: [edge] }
  }
}
policy {
  define PREFER-PRIMARY {
    rank 10: permit {
      match prefix 192.168.0.0/16 le 24
      set local-pref 300
      if neighbor.state == LIVE
    }
    rank 20: permit {
      match any
      set local-pref 100
    }
    rank 30: deny {
      match prefix 0.0.0.0/0 le 32
    }
  }
}
intent {
  CORE-TRAFFIC: route backbone {
    primary: edge >> spine >> leaf
    backup:  edge >> leaf
    apply-policy: PREFER-PRIMARY
    fault-tolerance: 2
    scope: all
  }
}
