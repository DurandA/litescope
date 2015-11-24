from litescope.common import *


class LiteScopeInOut(Module, AutoCSR):
    def __init__(self, dw):
        self.dw = dw
        self._input = CSRStatus(dw)
        self._output = CSRStorage(dw)

        self.i = self._input.status
        self.o = self._output.storage