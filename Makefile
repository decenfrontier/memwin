.PHONY: help build test

VERSION_FILE=memwin/version.py
VERSION='1.9.6'

write_version:
	@echo "version = $(VERSION)" > $(VERSION_FILE)


build: write_version
	@echo "Building memwin-$(VERSION)"
	@python setup.py sdist build
	@echo "Uploading to PyPI"
	@twine upload dist/memwin-$(VERSION).tar.gz


test:
	# pytest -s tests/test_xprocess.py -k "test_create_process"
	# pytest -s tests/test_xthread.py -k "test_get_pid"
	pytest -s tests/test_xapi.py -k "test_window_from_point"


help:
	@echo ""
	@echo "Usage:"
	@echo " make [target]"
	@echo ""
	@echo 'Targets:'
	@awk '/^[a-zA-Z\-_0-9]+:/ { \
	helpMessage = match(lastLine, /^# (.*)/); \
		if (helpMessage) { \
			helpCommand = substr($$1, 0, index($$1, ":")-1); \
			helpMessage = substr(lastLine, RSTART + 2, RLENGTH); \
			printf "\033[36m%-22s\033[0m %s\n", helpCommand,helpMessage; \
		} \
	} \
	{ lastLine = $$0 }' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help