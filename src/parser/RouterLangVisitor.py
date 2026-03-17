# Generated from src/grammar/RouterLang.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .RouterLangParser import RouterLangParser
else:
    from RouterLangParser import RouterLangParser

# This class defines a complete generic visitor for a parse tree produced by RouterLangParser.

class RouterLangVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RouterLangParser#program.
    def visitProgram(self, ctx:RouterLangParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#topoBlock.
    def visitTopoBlock(self, ctx:RouterLangParser.TopoBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#roleSection.
    def visitRoleSection(self, ctx:RouterLangParser.RoleSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#roleDecl.
    def visitRoleDecl(self, ctx:RouterLangParser.RoleDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#intRange.
    def visitIntRange(self, ctx:RouterLangParser.IntRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#linkSection.
    def visitLinkSection(self, ctx:RouterLangParser.LinkSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#linkDecl.
    def visitLinkDecl(self, ctx:RouterLangParser.LinkDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#deviceSection.
    def visitDeviceSection(self, ctx:RouterLangParser.DeviceSectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#deviceBinding.
    def visitDeviceBinding(self, ctx:RouterLangParser.DeviceBindingContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#deviceList.
    def visitDeviceList(self, ctx:RouterLangParser.DeviceListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#routingBlock.
    def visitRoutingBlock(self, ctx:RouterLangParser.RoutingBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#routingBody.
    def visitRoutingBody(self, ctx:RouterLangParser.RoutingBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#bgpBlock.
    def visitBgpBlock(self, ctx:RouterLangParser.BgpBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#asnDecl.
    def visitAsnDecl(self, ctx:RouterLangParser.AsnDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#roleAsn.
    def visitRoleAsn(self, ctx:RouterLangParser.RoleAsnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#neighborDecl.
    def visitNeighborDecl(self, ctx:RouterLangParser.NeighborDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#peerEntry.
    def visitPeerEntry(self, ctx:RouterLangParser.PeerEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#rrDecl.
    def visitRrDecl(self, ctx:RouterLangParser.RrDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#ospfBlock.
    def visitOspfBlock(self, ctx:RouterLangParser.OspfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#areaDecl.
    def visitAreaDecl(self, ctx:RouterLangParser.AreaDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#roleList.
    def visitRoleList(self, ctx:RouterLangParser.RoleListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#policyBlock.
    def visitPolicyBlock(self, ctx:RouterLangParser.PolicyBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#policyDef.
    def visitPolicyDef(self, ctx:RouterLangParser.PolicyDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#policyStanza.
    def visitPolicyStanza(self, ctx:RouterLangParser.PolicyStanzaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#rankClause.
    def visitRankClause(self, ctx:RouterLangParser.RankClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#actionKw.
    def visitActionKw(self, ctx:RouterLangParser.ActionKwContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#matchClause.
    def visitMatchClause(self, ctx:RouterLangParser.MatchClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#matchExpr.
    def visitMatchExpr(self, ctx:RouterLangParser.MatchExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#prefixExpr.
    def visitPrefixExpr(self, ctx:RouterLangParser.PrefixExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#setClause.
    def visitSetClause(self, ctx:RouterLangParser.SetClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#setExpr.
    def visitSetExpr(self, ctx:RouterLangParser.SetExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#condClause.
    def visitCondClause(self, ctx:RouterLangParser.CondClauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#guardExpr.
    def visitGuardExpr(self, ctx:RouterLangParser.GuardExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#condVal.
    def visitCondVal(self, ctx:RouterLangParser.CondValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#stateVal.
    def visitStateVal(self, ctx:RouterLangParser.StateValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#intentBlock.
    def visitIntentBlock(self, ctx:RouterLangParser.IntentBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#intentDecl.
    def visitIntentDecl(self, ctx:RouterLangParser.IntentDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#routeBody.
    def visitRouteBody(self, ctx:RouterLangParser.RouteBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#pathSpec.
    def visitPathSpec(self, ctx:RouterLangParser.PathSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#pathExpr.
    def visitPathExpr(self, ctx:RouterLangParser.PathExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#policyRef.
    def visitPolicyRef(self, ctx:RouterLangParser.PolicyRefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#ftSpec.
    def visitFtSpec(self, ctx:RouterLangParser.FtSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#scopeSpec.
    def visitScopeSpec(self, ctx:RouterLangParser.ScopeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#scopeVal.
    def visitScopeVal(self, ctx:RouterLangParser.ScopeValContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#constraintBody.
    def visitConstraintBody(self, ctx:RouterLangParser.ConstraintBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by RouterLangParser#transitionBlock.
    def visitTransitionBlock(self, ctx:RouterLangParser.TransitionBlockContext):
        return self.visitChildren(ctx)



del RouterLangParser