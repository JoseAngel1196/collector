# Run collector
.PHONY: run-collector
run-collector:
	PYTHONPATH=. python collector/runner.py

# Clean all pycache files
.PHONY: clean
clean:
	@find . -type d -name __pycache__ -exec rm -r {} \+

# Execute query
.PHONY: execute-db
execute-db:
	PYTHONPATH=. python scripts/db/create_tables.py
