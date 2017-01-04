import subprocess
import os
from os import chmod
import shutil
import tempfile


def git(*args):
    return subprocess.call(['git'] + list(args))


class GitFeatureImporter:

    def __init__(self, project):
        self.project = project

    def run(self):
        repo_path = 'repo-project-%d' % self.project.id
        feature_paths = self._get_feature_paths(repo_path)
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

    def _get_feature_paths(self, repo_path):
        if self.project.is_ssh_repo:
            fd, key_path = tempfile.mkstemp()

            file = os.fdopen(fd, 'w')
            file.write(self.project.private_key)
            file.close()
            chmod(key_path, 0o600)

            env = os.environ.copy()
            env["GIT_SSH_COMMAND"] = "ssh -o StrictHostKeyChecking=no -i %s" % key_path
            cmd = ["git", "clone", self.project.repo_url, repo_path]

            p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)

            stdout, stderr = p.communicate()

            if stdout:
                print(stdout)
            if stderr:
                print(stderr)

        else:
            git("clone", self.project.repo_url, repo_path)

        paths = []
        for root, dirs, files in os.walk("%s" % repo_path):
            for file in files:
                if file.endswith(".feature"):
                    paths.append(os.path.join(root, file))
        return paths