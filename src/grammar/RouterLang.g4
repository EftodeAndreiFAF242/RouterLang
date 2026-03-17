grammar RouterLang;

// ========== PARSER RULES ==========

program
    : topoBlock routingBlock policyBlock intentBlock transitionBlock? EOF
    ;

topoBlock
    : 'topology' '{' roleSection linkSection deviceSection? '}'
    ;

roleSection
    : 'roles' '{' roleDecl+ '}'
    ;

roleDecl
    : IDENT '{' 'count' ':' intRange '}'
    ;

intRange
    : INT ('..' INT)?
    ;

linkSection
    : 'links' '{' linkDecl+ '}'
    ;

linkDecl
    : IDENT '--' IDENT ('{' 'weight' ':' INT '}')?
    ;

deviceSection
    : 'devices' '{' deviceBinding+ '}'
    ;

deviceBinding
    : IDENT ':' '[' deviceList ']'
    ;

deviceList
    : IDENT (',' IDENT)*
    | IDENT '..' IDENT
    ;

routingBlock
    : 'routing' '{' routingBody '}'
    ;

routingBody
    : bgpBlock ospfBlock?
    | ospfBlock bgpBlock?
    ;

bgpBlock
    : 'bgp' '{' asnDecl neighborDecl? rrDecl? '}'
    ;

asnDecl
    : 'asn' '{' roleAsn+ '}'
    ;

roleAsn
    : IDENT ':' INT
    ;

neighborDecl
    : 'neighbors' ':' 'auto'
    | 'neighbors' '{' peerEntry+ '}'
    ;

peerEntry
    : IDENT ':' IPv4_ADDR
    ;

rrDecl
    : 'route-reflector' ':' IDENT
    ;

ospfBlock
    : 'ospf' '{' areaDecl+ '}'
    ;

areaDecl
    : 'area' INT '{' 'roles' ':' '[' roleList ']' '}'
    ;

roleList
    : IDENT (',' IDENT)*
    ;

policyBlock
    : 'policy' '{' policyDef+ '}'
    ;

policyDef
    : 'define' IDENT '{' policyStanza+ '}'
    ;

policyStanza
    : rankClause? actionKw '{' matchClause* setClause* condClause? '}'
    ;

rankClause
    : 'rank' INT ':'
    ;

actionKw
    : 'permit' | 'deny'
    ;

matchClause
    : 'match' matchExpr
    ;

matchExpr
    : 'prefix' prefixExpr
    | 'aspath' STRING
    | 'community' STRING
    | 'enter' '(' IDENT ')' 'and' 'exit' '(' IDENT ')'
    | 'any'
    ;

prefixExpr
    : CIDR ('le' INT)?
    ;

setClause
    : 'set' setExpr
    ;

setExpr
    : KW_LOCAL_PREF INT
    | 'metric' INT
    | 'community' STRING
    ;

condClause
    : 'if' guardExpr
    ;

guardExpr
    : IDENT '.' IDENT '==' condVal
    ;

condVal
    : stateVal
    | INT
    | STRING
    ;

stateVal
    : 'LIVE' | 'DRAINED' | 'WARM'
    ;

intentBlock
    : 'intent' '{' intentDecl+ '}'
    ;

intentDecl
    : IDENT ':' 'route' IDENT '{' routeBody '}'
    | IDENT ':' 'constraint' '{' constraintBody '}'
    ;

routeBody
    : pathSpec policyRef? ftSpec? scopeSpec?
    ;

pathSpec
    : 'primary' ':' pathExpr ('backup' ':' pathExpr)?
    ;

pathExpr
    : IDENT ('>>' IDENT)+
    ;

policyRef
    : 'apply-policy' ':' IDENT
    ;

ftSpec
    : 'fault-tolerance' ':' INT
    ;

scopeSpec
    : 'scope' ':' scopeVal
    ;

scopeVal
    : KW_ALL
    | KW_BORDER
    | IDENT (',' IDENT)*
    ;

constraintBody
    : policyRef scopeSpec?
    ;

transitionBlock
    : 'transition' '{' 'from' ':' IDENT 'to' ':' IDENT 'intermediate' ':' IDENT '}'
    ;

// ========== LEXER RULES ==========

KW_ALL        : 'all' ;
KW_BORDER     : 'border' ;
KW_LOCAL_PREF : 'local-preference' | 'local-pref' ;

IPv4_ADDR     : [0-9]+ '.' [0-9]+ '.' [0-9]+ '.' [0-9]+ ;
CIDR          : [0-9]+ '.' [0-9]+ '.' [0-9]+ '.' [0-9]+ '/' [0-9]+ ;
INT           : [0-9]+ ;
IDENT         : [a-zA-Z][a-zA-Z0-9_\-]* ;
STRING        : '"' (~["\\\r\n] | '\\' .)* '"' ;

WS            : [ \t\r\n]+ -> skip ;
LINE_CMT      : '//' ~[\n]* -> skip ;
BLOCK_CMT     : '/*' .*? '*/' -> skip ;