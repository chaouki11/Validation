
from Semantic import Semantic
 
class StepSynchComposition(Semantic):
    def __init__(self, lhs, rhs):
        self.lhs = lhs
        self.rhs = rhs

    def initial(self):
        initials = []
        for lhs_c in self.lhs.initial():
            for rhs_c in self.rhs.initial():
                c=lhs_c,rhs_c
                initials.append(c)
        return initials

    def actions(self, source):
        lhs_source,rhs_source=source
        syncActions = []
        lhs_actions = self.lhs.actions(lhs_source)
        action_count = len(lhs_actions)
        for lhs_action in lhs_actions:
            lhs_targets = self.lhs.execute(lhs_action, lhs_source)
            if len(lhs_targets)==0:
                action_count-=1
            for lhs_target in lhs_targets:
                lhs_step=(lhs_source,lhs_action,lhs_target)
                rhs_actions = self.rhs.actions(lhs_step, rhs_source)
                actions=map(lambda rA: (lhs_step,rA),rhs_actions)
                syncActions.extend(actions)    

        if action_count==0:
            lhs_step=lhs_source,"deadlock",lhs_source
            rhs_actions=self.rhs.actions(lhs_step,rhs_source)
            syncActions.extend(lambda rA: (lhs_step,rA),rhs_actions)

        return syncActions

    def execute(self,action, source):#might need to clear the confusion between the action and the piece
        lhs_step,rhs_action=action
        lhs_source,rhs_source=source
        rhs_targets=self.rhs.execute(rhs_action,lhs_step,rhs_source)

        return map(lambda rhs_target:(lhs_step[2],rhs_target),rhs_targets)
