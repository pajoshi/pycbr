from collections import defaultdict
import operator


class Aggregate:
    """An aggregation procedure to extract solutions from a set of cases"""

    def __init__(self):
        pass

    def aggregate(self, neighbours, similarity):
        """
        Aggregate a set of cases, possibly taking into account their similarities

        Args:
            neighbours (pandas.DataFrame): A dataframe with the most similar cases to aggregate.
            similarity (list of float): A list of the similarities of each case

        Returns:
            The aggregate solution

        """
        raise NotImplementedError


class MajorityAggregate(Aggregate):
    """Solution aggregation by majority, possible weighted by similarity"""

    def __init__(self, attribute, weighted=True):
        super().__init__()
        self.attribute = attribute
        self.weighted = weighted

        if isinstance(attribute, str) or isinstance(attribute, int):
            self._f = operator.itemgetter(attribute)
        else:
            self._f = attribute

    def aggregate(self, neighbours, similarity):
        d = defaultdict(lambda: 0)
        for (_, n), s in zip(neighbours.iterrows(), similarity):
            d[self._f(n)] += s if self.weighted else 1

        return max(d.items(), key=operator.itemgetter(1))[0]