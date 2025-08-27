from sklearn.impute import KNNImputer
from utils import load_question_meta
import numpy as np


questions = load_question_meta()


class SubjectWeightedKNNImputer(KNNImputer):

    def __init__(self, min_overlap=1, **kwargs):
        super().__init__(**kwargs)
        self.min_overlap = min_overlap
        self.overlap_matrix = None


    # We override the transform method to set our custom metrics
    def transform(self, X):
        self._precompute_overlaps()
        n_samples, n_features = X.shape

        imputed = X.copy()

        answered = ~np.isnan(X)

        for j in range(n_features):
            missing = np.where(np.isnan(X[:, j]))[0]
            candidates = np.where(answered[:, j])[0]

            for i in missing:
                distances = []
                predictions = []
                for k in candidates:
                    dist = self._subject_weighted_distance(X[i], X[k], j)
                    distances.append(dist)
                    predictions.append(X[k][j])

                imputed[i, j] = self.get_prediction(distances, predictions, self.n_neighbors)

        if np.isnan(imputed).any():
            raise ValueError("Imputation error: imputed matrix contains NaN value ")

        return imputed


    def _subject_weighted_distance(self, x, y, q_id):
        """ Custom metric described in the writeup.

        q_subjects is a set of subject_ids for the question we are imputing

        :param q_subjects: Set of ints
        """
        both_answered = ~np.isnan(x) & ~np.isnan(y)
        diffs = x[both_answered] != y[both_answered]
        weights = self.overlap_matrix[q_id, both_answered]

        relevant = weights > 0

        distance_squared = np.sum((weights[relevant & diffs]) ** 2)
        total_weight = np.sum(relevant)
        if total_weight > 0:
            return np.sqrt(len(x) * distance_squared / total_weight )
        return np.inf


    def _precompute_overlaps(self):
        """
        Pre-compute the set P for each question
        """
        if self.overlap_matrix is not None:
            return
        n = len(questions["subject_id"])
        self.overlap_matrix = np.zeros((n, n))

        for i in range(n):
            subjects = questions["subject_id"][i]
            for j in range(n):
                overlap = len(questions["subject_id"][j].intersection(subjects))
                if overlap >= self.min_overlap:
                    self.overlap_matrix[i, j] = overlap / len(subjects)


    def get_prediction(self, distances, predictions, k):
        """ Given an array of tuples (d, y) where d is the distance and y
        is the correctness of the question we are imputing, return the prediction
        for k nearest neighbors.

        Ex: distances = [(1, 1), (2, 0)], k = 1
        Returns 1

        :Param distances: list[tuple[float, int]]
        :Param k: int
        :Return: int

        distances = np.array(distances)
        predictions = np.array(predictions)

        smallest_distances = np.argpartition(distances, k)[:k]

        labels = predictions[smallest_distances]

        prediction = int(np.sum(labels) > k / 2)
        """
        distances = [(distances[i], predictions[i]) for i in range(len(predictions))]
        distances.sort(key=lambda x: x[0])
        n_nearest = [val for (dist, val) in distances[:self.n_neighbors]]

        return int(sum(n_nearest) > (self.n_neighbors / 2))
