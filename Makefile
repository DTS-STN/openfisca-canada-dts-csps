clean:
	rm -rf build dist
	find . -name '*.pyc' -exec rm \{\} \;

build-run-dev:
	docker-compose up --build --detach --force-recreate

build-run-dev-local:
	pip install .
	openfisca serve --port 5000 --country-package openfisca_canada_mvohwr

test:
	docker exec openfisca_dev openfisca test -c openfisca_canada_mvohwr openfisca_canada_mvohwr/tests

test-local:
	pip install .
	openfisca-run-test --country-package openfisca_canada_mvohwr openfisca_canada_mvohwr/tests