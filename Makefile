# Windows Makefile using PowerShell

.PHONY: run backend frontend clean

run:
	@start powershell -NoExit -Command "cd '$(CURDIR)' ; python main.py"
	@start powershell -NoExit -Command "cd '$(CURDIR)/virtual_cookbook_frontend' ; npm run dev"

backend:
	@start powershell -NoExit -Command "cd '$(CURDIR)' ; python main.py"

frontend:
	@start powershell -NoExit -Command "cd '$(CURDIR)/virtual_cookbook_frontend' ; npm run dev"

clean:
	@echo Cleaning up...
	@if exist __pycache__ rmdir /s /q __pycache__
	@if exist *.pyc del /s /q *.pyc
	@if exist virtual_cookbook_frontend\\dist rmdir /s /q virtual_cookbook_frontend\\dist
	@echo Done.