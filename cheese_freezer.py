from pip import req as pip_req, index, log as pip_log
import argparse
import tempfile
import shutil
import os
import sys


def parse_arguments():
    parser = argparse.ArgumentParser(description="Cheese-Freezer")
    parser.add_argument("x_file", help="Requirements file")
    parser.add_argument(
        '--skip-requirements-regex',
        dest='skip_requirements_regex',
        default='')
    parser.add_argument("-d", "--download-dir", dest="x_download", default='',
        help="Only download requirements, don't do install or upload")
    return parser.parse_args()


def main():
    args = parse_arguments()
    
    # show some output
    pip_log.logger.consumers.extend([(pip_log.logger.level_for_integer(3), sys.stdout)])

    finder = index.PackageFinder([], [], use_mirrors=True)
    reqs = pip_req.parse_requirements(args.x_file, finder=finder, options=args)
 
    tmpdir = tempfile.mkdtemp(prefix='cheese')
    try:
        for d in ("build", "src"):
            os.mkdir(os.path.join(tmpdir, d))
        req_set = pip_req.RequirementSet(
            build_dir=os.path.join(tmpdir, "build"),
            src_dir=os.path.join(tmpdir, "src"),
            download_dir=args.x_download)
        req_set.ignore_installed = True
        for req in reqs:
            req_set.add_requirement(req)
        req_set.prepare_files(finder)
        if args.x_download:
            return
    finally:
        shutil.rmtree(tmpdir)
        pass


if __name__ == "__main__":
    main()
