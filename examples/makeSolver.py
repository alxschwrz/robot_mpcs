import os
import sys
sys.path.insert(0, '/Users/Alex/develop/forces_pro_client')
from robotmpcs.models.pointRobotMpcModel import PointRobotMpcModel
from robotmpcs.models.planarArmMpcModel import PlanarArmMpcModel
from robotmpcs.models.diffDriveMpcModel import DiffDriveMpcModel
from robotmpcs.models.pandaMpcModel import PandaMpcModel


def main():
    N = 20
    m = 3
    dt = 0.01
    #mpcModel = PlanarArmMpcModel(m, N, 4)
    #mpcModel = PointRobotMpcModel(m, N)
    #mpcModel = DiffDriveMpcModel(2, N)
    mpcModel = PandaMpcModel(m, N)
    mpcModel.setDt(dt)
    #mpcModel.setSlack()
    mpcModel.setObstacles(0, 3)
    mpcModel.setModel()
    mpcModel.setCodeoptions()
    path_to_solvers = os.path.dirname(os.path.abspath(__file__)) + '/solvers/'
    mpcModel.generateSolver(location=path_to_solvers)


if __name__ == "__main__":
    main()
