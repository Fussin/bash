.DEFAULT_GOAL := help

# Delegate all tasks to the Taskfile runner
# This allows using `make up` as an alias for `task up`
%:
	@task $@

help:
	@echo "See all available commands by running: task --list"
	@task --list

.PHONY: help
