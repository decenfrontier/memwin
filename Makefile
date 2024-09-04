.PHONY: help build test

VERSION_FILE=version.py
VERSION='1.7.0'

write_version:
	@echo "version = $(VERSION)" > $(VERSION_FILE)


build: write_version
	@python setup.py sdist build
	@twine upload dist/*


test:
	# pytest -s tests/test_xprocess.py -k "test_create_process"
	pytest -s tests/test_xapi.py -k "test_set_system_cursor"


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