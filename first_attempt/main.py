import nuralnet
import FUNC

nuralnet.Construct(
        2,
        nuralnet.Layer(4),
        FUNC.relu,
        nuralnet.Layer(4),
        FUNC.tanh
        )
