import subprocess
import os
import shutil


def git(*args):
    return subprocess.call(['git'] + list(args))


class GitFeatureImporter:

    def __init__(self, project):
        self.project = project

    def run(self):
        repo_path = 'repo-project-%d' % self.project.id
        feature_paths = self.get_feature_paths(repo_path)
        features_root_path = os.path.commonprefix(feature_paths)

        for path in feature_paths:
            feature_name = path.replace(features_root_path, '')
            feature_file = open(path, 'r')
            feature_body = feature_file.read()

            self.project.features.create(
                project=self.project,
                name=feature_name,
                body=feature_body
            )

        shutil.rmtree(repo_path)

        return features_root_path.replace(repo_path, '')

    def get_feature_paths(self, repo_path):
        git("clone", self.project.repo_url, repo_path)

        paths = []
        for root, dirs, files in os.walk("%s" % repo_path):
            for file in files:
                if file.endswith(".feature"):
                    paths.append(os.path.join(root, file))
        return paths