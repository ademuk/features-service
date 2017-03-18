import subprocess
import os
import shutil
import tempfile


def git(*args):
    return subprocess.call(['git'] + list(args))


def find_feature_paths(project, repo_path):
    if project.is_ssh_repo:
        fd, key_path = tempfile.mkstemp()

        file = os.fdopen(fd, 'w')
        file.write(project.private_key)
        file.close()
        os.chmod(key_path, 0o600)

        env = os.environ.copy()

        app_root = os.path.dirname(os.path.realpath(__file__))

        env["GIT_SSH"] = os.path.join(app_root, 'bin', 'ssh.sh')
        env["PRIVATE_KEY"] = key_path
        cmd = ["git", "clone", project.repo_url, repo_path]

        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=env)

        stdout, stderr = p.communicate()

        if stdout:
            print(stdout)
        if stderr:
            print(stderr)

    else:
        git("clone", project.repo_url, repo_path)

    paths = []
    for root, dirs, files in os.walk("%s" % repo_path):
        for file in files:
            if file.endswith(".feature"):
                paths.append(os.path.join(root, file))
    return paths


def open_features(paths, root_path):
    features = []
    for path in paths:
        name = path.replace(root_path, '')
        with open(path, 'r') as feature_file:
            body = feature_file.read()
        features.append((name, body))
    return features

class GitFeatureImporter:

    def __init__(self, project):
        self.project = project

    def run(self):
        repo_path = 'repo-project-%d' % self.project.id
        feature_paths = find_feature_paths(self.project, repo_path)
        features_root_path = os.path.commonprefix(feature_paths)
        features_path = features_root_path.replace(repo_path, '')

        features = open_features(feature_paths, features_root_path)
        self.project.update_features(features)

        shutil.rmtree(repo_path)

        return features_path
