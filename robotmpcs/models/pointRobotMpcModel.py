from robotmpcs.models.mpcModel import MpcModel
from forwardkinematics.fksCommon.fk_creator import FkCreator


class PointRobotMpcModel(MpcModel):

    def __init__(self, dim_goal, time_horizon):
        dof = 2
        super().__init__(dim_goal, dof, time_horizon)
        self._fk = FkCreator('pointMass', dof).fk()
        self._modelName = 'pointRobot'

