import jsonpath_rw as jsonpath
import operator


class SimpleCondition(object):
    op = None

    def check(self, value, expected):
        return self.op(value, expected)
        

class EqCondition(SimpleCondition):
    op = operator.eq

OPERATORS = {
  'eq': EqCondition,
}

class BaseRule(object):

    def __init__(self, field, op, val, multiple='first'):
        self.field = field
        self.op = op
        self.value = val
        self.multiple = multiple

    def check(self, pillar):
        """Check if condition match in the passed pillar.

        :param pillar: pillar data to check for condition in.
        :return: True if condition match, False otherwise.
        """

        res = False
        count = 0
        for match in jsonpath.parse(self.field).find(pillar):
            cond_ext = OPERATORS[self.op]()
            res = cond_ext.check(match.value, self.value)
            if (self.multiple == 'first' or
                (self.multiple == 'all' and not res) or
                (self.multiple == 'any' and res)):
                    break
            elif self.multiple == 'multiple' and res:
                count += 1
                if count > 1:
                    return True

        if not res or self.multiple == 'multiple':
            return False

        return True
