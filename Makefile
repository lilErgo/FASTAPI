.DEFAULT_GOAL := help

HOST ?= 127.0.0.1
PORT ?= 8000

run: #start uvicorn
	poetry uvicorn main:app --host $(HOST) --port $(PORT)
I
install: #install
	@echo "Installing dependency $(LIBRARY)"
	poetry add $(LIBRARY)

uninstall: #uninstall
	@echo: "Uninstalling dependency $(LIBRARY)"

help: #show this help message
	@echo "Usege: make [command]"
	@echo ""
	@echo "Commands:"
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE) | awk 'BEGIN {FS = ":.*?## "}; {printf " %-20s %s\n" $$1, $$2}'