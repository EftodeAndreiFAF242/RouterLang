# Generated from src/grammar/RouterLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RouterLangParser import RouterLangParser
else:
    from RouterLangParser import RouterLangParser

# This class defines a complete listener for a parse tree produced by RouterLangParser.
class RouterLangListener(ParseTreeListener):

    # Enter a parse tree produced by RouterLangParser#program.
    def enterProgram(self, ctx:RouterLangParser.ProgramContext):
        pass

    # Exit a parse tree produced by RouterLangParser#program.
    def exitProgram(self, ctx:RouterLangParser.ProgramContext):
        pass


    # Enter a parse tree produced by RouterLangParser#topoBlock.
    def enterTopoBlock(self, ctx:RouterLangParser.TopoBlockContext):
        pass

    # Exit a parse tree produced by RouterLangParser#topoBlock.
    def exitTopoBlock(self, ctx:RouterLangParser.TopoBlockContext):
        pass


    # Enter a parse tree produced by RouterLangParser#roleSection.
    def enterRoleSection(self, ctx:RouterLangParser.RoleSectionContext):
        pass

    # Exit a parse tree produced by RouterLangParser#roleSection.
    def exitRoleSection(self, ctx:RouterLangParser.RoleSectionContext):
        pass


    # Enter a parse tree produced by RouterLangParser#roleDecl.
    def enterRoleDecl(self, ctx:RouterLangParser.RoleDeclContext):
        pass

    # Exit a parse tree produced by RouterLangParser#roleDecl.
    def exitRoleDecl(self, ctx:RouterLangParser.RoleDeclContext):
        pass


    # Enter a parse tree produced by RouterLangParser#intRange.
    def enterIntRange(self, ctx:RouterLangParser.IntRangeContext):
        pass

    # Exit a parse tree produced by RouterLangParser#intRange.
    def exitIntRange(self, ctx:RouterLangParser.IntRangeContext):
        pass


    # Enter a parse tree produced by RouterLangParser#linkSection.
    def enterLinkSection(self, ctx:RouterLangParser.LinkSectionContext):
        pass

    # Exit a parse tree produced by RouterLangParser#linkSection.
    def exitLinkSection(self, ctx:RouterLangParser.LinkSectionContext):
        pass


    # Enter a parse tree produced by RouterLangParser#linkDecl.
    def enterLinkDecl(self, ctx:RouterLangParser.LinkDeclContext):
        pass

    # Exit a parse tree produced by RouterLangParser#linkDecl.
    def exitLinkDecl(self, ctx:RouterLangParser.LinkDeclContext):
        pass


    # Enter a parse tree produced by RouterLangParser#deviceSection.
    def enterDeviceSection(self, ctx:RouterLangParser.DeviceSectionContext):
        pass

    # Exit a parse tree produced by RouterLangParser#deviceSection.
    def exitDeviceSection(self, ctx:RouterLangParser.DeviceSectionContext):
        pass


    # Enter a parse tree produced by RouterLangParser#deviceBinding.
    def enterDeviceBinding(self, ctx:RouterLangParser.DeviceBindingContext):
        pass

    # Exit a parse tree produced by RouterLangParser#deviceBinding.
    def exitDeviceBinding(self, ctx:RouterLangParser.DeviceBindingContext):
        pass


    # Enter a parse tree produced by RouterLangParser#deviceList.
    def enterDeviceList(self, ctx:RouterLangParser.DeviceListContext):
        pass

    # Exit a parse tree produced by RouterLangParser#deviceList.
    def exitDeviceList(self, ctx:RouterLangParser.DeviceListContext):
        pass


    # Enter a parse tree produced by RouterLangParser#routingBlock.
    def enterRoutingBlock(self, ctx:RouterLangParser.RoutingBlockContext):
        pass

    # Exit a parse tree produced by RouterLangParser#routingBlock.
    def exitRoutingBlock(self, ctx:RouterLangParser.RoutingBlockContext):
        pass


    # Enter a parse tree produced by RouterLangParser#routingBody.
    def enterRoutingBody(self, ctx:RouterLangParser.RoutingBodyContext):
        pass

    # Exit a parse tree produced by RouterLangParser#routingBody.
    def exitRoutingBody(self, ctx:RouterLangParser.RoutingBodyContext):
        pass


    # Enter a parse tree produced by RouterLangParser#bgpBlock.
    def enterBgpBlock(self, ctx:RouterLangParser.BgpBlockContext):
        pass

    # Exit a parse tree produced by RouterLangParser#bgpBlock.
    def exitBgpBlock(self, ctx:RouterLangParser.BgpBlockContext):
        pass


    # Enter a parse tree produced by RouterLangParser#asnDecl.
    def enterAsnDecl(self, ctx:RouterLangParser.AsnDeclContext):
        pass

    # Exit a parse tree produced by RouterLangParser#asnDecl.
    def exitAsnDecl(self, ctx:RouterLangParser.AsnDeclContext):
        pass


    # Enter a parse tree produced by RouterLangParser#roleAsn.
    def enterRoleAsn(self, ctx:RouterLangParser.RoleAsnContext):
        pass

    # Exit a parse tree produced by RouterLangParser#roleAsn.
    def exitRoleAsn(self, ctx:RouterLangParser.RoleAsnContext):
        pass


    # Enter a parse tree produced by RouterLangParser#neighborDecl.
    def enterNeighborDecl(self, ctx:RouterLangParser.NeighborDeclContext):
        pass

    # Exit a parse tree produced by RouterLangParser#neighborDecl.
    def exitNeighborDecl(self, ctx:RouterLangParser.NeighborDeclContext):
        pass


    # Enter a parse tree produced by RouterLangParser#peerEntry.
    def enterPeerEntry(self, ctx:RouterLangParser.PeerEntryContext):
        pass

    # Exit a parse tree produced by RouterLangParser#peerEntry.
    def exitPeerEntry(self, ctx:RouterLangParser.PeerEntryContext):
        pass


    # Enter a parse tree produced by RouterLangParser#rrDecl.
    def enterRrDecl(self, ctx:RouterLangParser.RrDeclContext):
        pass

    # Exit a parse tree produced by RouterLangParser#rrDecl.
    def exitRrDecl(self, ctx:RouterLangParser.RrDeclContext):
        pass


    # Enter a parse tree produced by RouterLangParser#ospfBlock.
    def enterOspfBlock(self, ctx:RouterLangParser.OspfBlockContext):
        pass

    # Exit a parse tree produced by RouterLangParser#ospfBlock.
    def exitOspfBlock(self, ctx:RouterLangParser.OspfBlockContext):
        pass


    # Enter a parse tree produced by RouterLangParser#areaDecl.
    def enterAreaDecl(self, ctx:RouterLangParser.AreaDeclContext):
        pass

    # Exit a parse tree produced by RouterLangParser#areaDecl.
    def exitAreaDecl(self, ctx:RouterLangParser.AreaDeclContext):
        pass


    # Enter a parse tree produced by RouterLangParser#roleList.
    def enterRoleList(self, ctx:RouterLangParser.RoleListContext):
        pass

    # Exit a parse tree produced by RouterLangParser#roleList.
    def exitRoleList(self, ctx:RouterLangParser.RoleListContext):
        pass


    # Enter a parse tree produced by RouterLangParser#policyBlock.
    def enterPolicyBlock(self, ctx:RouterLangParser.PolicyBlockContext):
        pass

    # Exit a parse tree produced by RouterLangParser#policyBlock.
    def exitPolicyBlock(self, ctx:RouterLangParser.PolicyBlockContext):
        pass


    # Enter a parse tree produced by RouterLangParser#policyDef.
    def enterPolicyDef(self, ctx:RouterLangParser.PolicyDefContext):
        pass

    # Exit a parse tree produced by RouterLangParser#policyDef.
    def exitPolicyDef(self, ctx:RouterLangParser.PolicyDefContext):
        pass


    # Enter a parse tree produced by RouterLangParser#policyStanza.
    def enterPolicyStanza(self, ctx:RouterLangParser.PolicyStanzaContext):
        pass

    # Exit a parse tree produced by RouterLangParser#policyStanza.
    def exitPolicyStanza(self, ctx:RouterLangParser.PolicyStanzaContext):
        pass


    # Enter a parse tree produced by RouterLangParser#rankClause.
    def enterRankClause(self, ctx:RouterLangParser.RankClauseContext):
        pass

    # Exit a parse tree produced by RouterLangParser#rankClause.
    def exitRankClause(self, ctx:RouterLangParser.RankClauseContext):
        pass


    # Enter a parse tree produced by RouterLangParser#actionKw.
    def enterActionKw(self, ctx:RouterLangParser.ActionKwContext):
        pass

    # Exit a parse tree produced by RouterLangParser#actionKw.
    def exitActionKw(self, ctx:RouterLangParser.ActionKwContext):
        pass


    # Enter a parse tree produced by RouterLangParser#matchClause.
    def enterMatchClause(self, ctx:RouterLangParser.MatchClauseContext):
        pass

    # Exit a parse tree produced by RouterLangParser#matchClause.
    def exitMatchClause(self, ctx:RouterLangParser.MatchClauseContext):
        pass


    # Enter a parse tree produced by RouterLangParser#matchExpr.
    def enterMatchExpr(self, ctx:RouterLangParser.MatchExprContext):
        pass

    # Exit a parse tree produced by RouterLangParser#matchExpr.
    def exitMatchExpr(self, ctx:RouterLangParser.MatchExprContext):
        pass


    # Enter a parse tree produced by RouterLangParser#prefixExpr.
    def enterPrefixExpr(self, ctx:RouterLangParser.PrefixExprContext):
        pass

    # Exit a parse tree produced by RouterLangParser#prefixExpr.
    def exitPrefixExpr(self, ctx:RouterLangParser.PrefixExprContext):
        pass


    # Enter a parse tree produced by RouterLangParser#setClause.
    def enterSetClause(self, ctx:RouterLangParser.SetClauseContext):
        pass

    # Exit a parse tree produced by RouterLangParser#setClause.
    def exitSetClause(self, ctx:RouterLangParser.SetClauseContext):
        pass


    # Enter a parse tree produced by RouterLangParser#setExpr.
    def enterSetExpr(self, ctx:RouterLangParser.SetExprContext):
        pass

    # Exit a parse tree produced by RouterLangParser#setExpr.
    def exitSetExpr(self, ctx:RouterLangParser.SetExprContext):
        pass


    # Enter a parse tree produced by RouterLangParser#condClause.
    def enterCondClause(self, ctx:RouterLangParser.CondClauseContext):
        pass

    # Exit a parse tree produced by RouterLangParser#condClause.
    def exitCondClause(self, ctx:RouterLangParser.CondClauseContext):
        pass


    # Enter a parse tree produced by RouterLangParser#guardExpr.
    def enterGuardExpr(self, ctx:RouterLangParser.GuardExprContext):
        pass

    # Exit a parse tree produced by RouterLangParser#guardExpr.
    def exitGuardExpr(self, ctx:RouterLangParser.GuardExprContext):
        pass


    # Enter a parse tree produced by RouterLangParser#condVal.
    def enterCondVal(self, ctx:RouterLangParser.CondValContext):
        pass

    # Exit a parse tree produced by RouterLangParser#condVal.
    def exitCondVal(self, ctx:RouterLangParser.CondValContext):
        pass


    # Enter a parse tree produced by RouterLangParser#stateVal.
    def enterStateVal(self, ctx:RouterLangParser.StateValContext):
        pass

    # Exit a parse tree produced by RouterLangParser#stateVal.
    def exitStateVal(self, ctx:RouterLangParser.StateValContext):
        pass


    # Enter a parse tree produced by RouterLangParser#intentBlock.
    def enterIntentBlock(self, ctx:RouterLangParser.IntentBlockContext):
        pass

    # Exit a parse tree produced by RouterLangParser#intentBlock.
    def exitIntentBlock(self, ctx:RouterLangParser.IntentBlockContext):
        pass


    # Enter a parse tree produced by RouterLangParser#intentDecl.
    def enterIntentDecl(self, ctx:RouterLangParser.IntentDeclContext):
        pass

    # Exit a parse tree produced by RouterLangParser#intentDecl.
    def exitIntentDecl(self, ctx:RouterLangParser.IntentDeclContext):
        pass


    # Enter a parse tree produced by RouterLangParser#routeBody.
    def enterRouteBody(self, ctx:RouterLangParser.RouteBodyContext):
        pass

    # Exit a parse tree produced by RouterLangParser#routeBody.
    def exitRouteBody(self, ctx:RouterLangParser.RouteBodyContext):
        pass


    # Enter a parse tree produced by RouterLangParser#pathSpec.
    def enterPathSpec(self, ctx:RouterLangParser.PathSpecContext):
        pass

    # Exit a parse tree produced by RouterLangParser#pathSpec.
    def exitPathSpec(self, ctx:RouterLangParser.PathSpecContext):
        pass


    # Enter a parse tree produced by RouterLangParser#pathExpr.
    def enterPathExpr(self, ctx:RouterLangParser.PathExprContext):
        pass

    # Exit a parse tree produced by RouterLangParser#pathExpr.
    def exitPathExpr(self, ctx:RouterLangParser.PathExprContext):
        pass


    # Enter a parse tree produced by RouterLangParser#policyRef.
    def enterPolicyRef(self, ctx:RouterLangParser.PolicyRefContext):
        pass

    # Exit a parse tree produced by RouterLangParser#policyRef.
    def exitPolicyRef(self, ctx:RouterLangParser.PolicyRefContext):
        pass


    # Enter a parse tree produced by RouterLangParser#ftSpec.
    def enterFtSpec(self, ctx:RouterLangParser.FtSpecContext):
        pass

    # Exit a parse tree produced by RouterLangParser#ftSpec.
    def exitFtSpec(self, ctx:RouterLangParser.FtSpecContext):
        pass


    # Enter a parse tree produced by RouterLangParser#scopeSpec.
    def enterScopeSpec(self, ctx:RouterLangParser.ScopeSpecContext):
        pass

    # Exit a parse tree produced by RouterLangParser#scopeSpec.
    def exitScopeSpec(self, ctx:RouterLangParser.ScopeSpecContext):
        pass


    # Enter a parse tree produced by RouterLangParser#scopeVal.
    def enterScopeVal(self, ctx:RouterLangParser.ScopeValContext):
        pass

    # Exit a parse tree produced by RouterLangParser#scopeVal.
    def exitScopeVal(self, ctx:RouterLangParser.ScopeValContext):
        pass


    # Enter a parse tree produced by RouterLangParser#constraintBody.
    def enterConstraintBody(self, ctx:RouterLangParser.ConstraintBodyContext):
        pass

    # Exit a parse tree produced by RouterLangParser#constraintBody.
    def exitConstraintBody(self, ctx:RouterLangParser.ConstraintBodyContext):
        pass


    # Enter a parse tree produced by RouterLangParser#transitionBlock.
    def enterTransitionBlock(self, ctx:RouterLangParser.TransitionBlockContext):
        pass

    # Exit a parse tree produced by RouterLangParser#transitionBlock.
    def exitTransitionBlock(self, ctx:RouterLangParser.TransitionBlockContext):
        pass



del RouterLangParser