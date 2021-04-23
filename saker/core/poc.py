from saker.core.sess import Sess


class PoC(Sess):

    def __init__(self):
        super(PoC, self).__init__()

    def _verify(self, target):
        raise Exception("Not Imple")

    def verify(self, target):
        ret = self._verify(target)
        if ret:
            self.logger.debug("run %s success" % target)
        else:
            self.logger.debug("run %s fail" % target)
