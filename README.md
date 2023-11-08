# cross-platform-ci

run flake8 in CI: Do not need o run only on code changes; run on full files, but do not include this status check as required to pass for the pull request to merge. In branch protection rule, only set run-tests yml status check as reuqired to pass for the branch to be allowed to merge. This way linting errors can be seen but they will not affect pull request merge. motivation is to turn the red cross to green tick.
