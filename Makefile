
DIST=./dist/vhdw/vhdw 

$(DIST): vhdw.py vhd.py utils.py vhdw.spec 


vhdw.spec: 
	pyinstaller -i vhdw.py 


.PHONY: clean install  

clean:
	-rm -r ./build ./dist 

install:
	sudo cp $(DIST) /usr/bin/
	sudo cp -r ./dist/vhdw/_internal /usr/bin/

uninstall:
	sudo rm /usr/bin/vhdw 
	sudo rm -r  /usr/bin/_internal/
