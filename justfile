alias l := lock
alias i := install
alias u := uninstall
alias c := clean

lock:
	uv pip freeze | uv pip compile - -o requirements.txt
install:
	uv pip install -e .
uninstall:
	uv pip uninstall qrgenerator
clean:
	rm -rf *.egg-info .ruff_cache
