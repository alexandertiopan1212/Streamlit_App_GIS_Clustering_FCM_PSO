import numpy as np
from sklearn.metrics import davies_bouldin_score
from sklearn.metrics import silhouette_score
from fcmeans import FCM
import pandas as pd
import streamlit as st

from particle import Particle

class PSOClustering:
    def __init__(self, n_clusters: int, n_particles: int, data: np.ndarray, w=0.1, c1=1.5, c2=1.5):
        self.n_clusters = n_clusters
        self.n_particles = n_particles
        self.data = data
        self.particles = []
        self.gb_pos = None
        self.gb_val = np.inf
        self.gb_clustering = None
        self._generate_particles(w, c1, c2)

    def _generate_particles(self, w: float, c1: float, c2: float):
        for i in range(self.n_particles):
            particle = Particle(n_clusters=self.n_clusters, data=self.data, w=w, c1=c1, c2=c2)
            self.particles.append(particle)

    def update_gb(self, particle):
        if particle.pb_val < self.gb_val:
            self.gb_val = particle.pb_val
            self.gb_pos = particle.pb_pos.copy()
            self.gb_clustering = particle.pb_clustering.copy()

    def print_indices(self, data_points):
        score1 = davies_bouldin_score(self.data, data_points.clus)

        score2 = silhouette_score(self.data, data_points.clus)
        return score1, score2

    def start(self, iteration):
        pred_result = []
        score = []
        progress = []
        for i in range(iteration):
            for particle in self.particles:
                particle.update_pb(data=self.data)
                self.update_gb(particle=particle)

            for particle in self.particles:
                particle.move_centroids(gb_pos=self.gb_pos)
            progress.append([self.gb_pos, self.gb_clustering, self.gb_val])

            if i == iteration - 1:
                clusters = self.gb_clustering
                df = pd.DataFrame(self.data)
                x_y = pd.concat([df, pd.DataFrame(clusters, columns=['clus'])], axis=1)
                x_y["clus"] = x_y.clus.astype('category')
                pred_result.append(x_y["clus"])
                score.append(self.print_indices(x_y))

            elif i % 100 == 0:
                clusters = self.gb_clustering
                df = pd.DataFrame(self.data)
                x_y = pd.concat([df, pd.DataFrame(clusters, columns=['clus'])], axis=1)
                x_y["clus"] = x_y.clus.astype('category')
                pred_result.append(x_y["clus"])
                score.append(self.print_indices(x_y))


        f_cmeans = FCM(n_clusters=self.n_clusters, max_iter=100, n_init=2)
        f_cmeans.fit(self.data)
        f_cmeans_result = f_cmeans.predict(self.data)
        df = pd.DataFrame(self.data)
        x_y = pd.concat([df, pd.DataFrame(f_cmeans_result, columns=['clus'])], axis=1)
        x_y["clus"] = x_y.clus.astype('category')
        pred_result.append(x_y["clus"])
        score.append(self.print_indices(x_y))

        return pred_result, score