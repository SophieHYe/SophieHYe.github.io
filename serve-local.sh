#!/usr/bin/env bash
# Local preview for the Jekyll site on this pod.
# Ruby/Jekyll come from a conda env (rubygems.org is blocked by the egress
# allowlist, so gems were installed from conda-forge as rb-* packages instead
# of via `bundle install`). Bundler is skipped via JEKYLL_NO_BUNDLER_REQUIRE.
set -euo pipefail

source /opt/conda/etc/profile.d/conda.sh
conda activate jekyll

cd "$(dirname "$0")"
export JEKYLL_NO_BUNDLER_REQUIRE=1

exec jekyll serve \
  --config _config.yml,_config_docker.yml \
  --host 0.0.0.0 --port "${PORT:-4000}" \
  --livereload --livereload-port 35729
